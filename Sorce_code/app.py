import os
import io
import pdfkit
import base64
import matplotlib.pyplot as plt
import time
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, jsonify

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'  # This is needed for secure sessions

# Function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    uploaded_file = None  # Initialize the uploaded file variable
    if request.method == "POST":
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            uploaded_file = filename  # Pass the uploaded filename
            flash(f'File "{filename}" uploaded successfully')  # Message after success
    
    return render_template("index.html", uploaded_file=uploaded_file)

# Route for running FAHP steps and updating the sidebar
@app.route('/run_fahp', methods=["POST"])
def run_fahp():
    step = request.json.get('step')
    
    # Simulate some time taken for each step (you can replace this with real step execution)
    time.sleep(2)  # This is to simulate the step running

    response = {
        'message': f"Step {step} completed",
        'next_step': step + 1 if step < 4 else None  # Simulate 4 steps
    }
    return jsonify(response)

# Serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
