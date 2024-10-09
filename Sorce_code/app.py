from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'  # Folder to save uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Route for the homepage (upload form)
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle file upload
@app.route('/upload_quartile', methods=['POST'])
def upload_quartile_file():
    if request.method == 'POST':
        file = request.files['file']  # Get the uploaded file
        if file:
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)  # Save the file to the uploads folder
            return f'File {filename} uploaded successfully!'  # For now, just return this message
    return redirect(url_for('home'))
# Step 2: Process the uploaded quartile file
@app.route('/process_quartile/<filename>')
def process_quartile(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Load the Excel file using pandas
    quartile_data = pd.read_excel(filepath)
    
    # Display the first few rows of the quartile data to check it loaded correctly
    quartile_preview = quartile_data.head().to_html()  # Convert the DataFrame to HTML for rendering

    # For now, just show the first few rows of the data on the results page
    return render_template('results.html', quartile_preview=quartile_preview)
if __name__ == '__main__':
    app.run(debug=True)
