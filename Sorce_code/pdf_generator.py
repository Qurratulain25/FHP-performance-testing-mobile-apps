from fpdf import FPDF

# Function to generate PDF report
def generate_pdf_report(priority_weights, filename):
    # Create a PDF document
    pdf = FPDF()
    pdf.add_page()

    # Title for the report
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=f"FAHP Results for {filename}", ln=True, align='C')

    # Add some spacing
    pdf.ln(10)

    # Subtitle
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Priority Weights:", ln=True, align='L')

    # Content (criteria and weights)
    pdf.set_font("Arial", size=10)
    for criterion, weight in priority_weights.items():
        pdf.cell(200, 10, txt=f"{criterion}: {weight:.4f}", ln=True, align='L')

    # Add another space before ending
    pdf.ln(10)

    # Save the PDF to a file
    pdf_path = f"{filename.split('.')[0]}_FAHP_report.pdf"
    pdf.output(pdf_path)

    print(f"PDF Report saved at {pdf_path}")
    return pdf_path
