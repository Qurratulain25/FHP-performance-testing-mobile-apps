import os
from fpdf import FPDF
import base64

# Function to convert the image to base64 format
def convert_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_image

# Function to generate PDF report
def generate_pdf_report(priority_weights, criteria, linguistic_weights, plot_path, filename):
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Title of the PDF
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="FAHP Analytical Hierarchy Report", ln=True, align='C')

    # Step 1: Criteria
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Step 1: Criteria Set", ln=True)
    pdf.set_font("Arial", size=10)
    for criterion in criteria:
        pdf.cell(200, 10, txt=criterion, ln=True)

    # Step 2: Linguistic Weights
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Step 2: Linguistic Weights Assigned", ln=True)
    pdf.set_font("Arial", size=10)
    for weight in linguistic_weights:
        pdf.cell(200, 10, txt=weight, ln=True)

    # Step 3: Priority Weights (FAHP results)
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Step 3: Fuzzy Synthetic Extent Calculated", ln=True)
    pdf.set_font("Arial", size=10)
    for criterion, weight in priority_weights.items():
        pdf.cell(200, 10, txt=f"{criterion}: {weight:.4f}", ln=True)

    # Graph (convert image to base64 and embed it)
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Graphical Results", ln=True)
    encoded_image = convert_image_to_base64(plot_path)
    pdf.ln(5)
    pdf.image(plot_path, w=180, h=100)  # Adjust size as needed

    # Save the PDF file
    pdf_path = f"{filename.split('.')[0]}_FAHP_Report.pdf"
    pdf.output(pdf_path)

    print(f"PDF Report saved at {pdf_path}")
    return pdf_path
