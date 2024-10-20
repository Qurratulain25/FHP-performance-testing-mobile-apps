import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
from werkzeug.utils import secure_filename
from fahp_utils import run_fahp_process, save_results_to_csv_and_visualize
from pdf_generator import generate_pdf_report

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
ALLOWED_EXTENSIONS = {'xlsx'}

# Check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home route - handles file upload
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return jsonify({"success": True, "filename": filename}), 200
    return render_template("index.html")

# Run FAHP process and return results
@app.route("/run_fahp", methods=["POST"])
def run_fahp():
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], request.json['filename'])
    custom_criteria = request.json['custom_criteria']
    linguistic_weights = request.json['linguistic_weights']

    # Call the FAHP processing function
    priority_weights, results_path, graph_path = run_fahp_process(file_path, custom_criteria, linguistic_weights)

    return jsonify({
        "success": True,
        "priority_weights": priority_weights,
        "results_path": results_path,
        "graph_path": graph_path
    })

# # Download the PDF report
@app.route("/download_pdf", methods=["POST"])
def download_pdf():
    filename = request.json['filename']
    criteria = request.json['criteria']  # Assuming these are passed from the frontend
    linguistic_weights = request.json['linguistic_weights']
    priority_weights = request.json['priority_weights']  # FAHP results
    plot_path = request.json['plot_path']  # Path to the plot image

    pdf_path = generate_pdf_report(priority_weights, criteria, linguistic_weights, plot_path, filename)
    return send_file(pdf_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
