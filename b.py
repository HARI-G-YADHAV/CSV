import pdfkit

def html_to_pdf(html_file, pdf_file):
    try:
        pdfkit.from_file(html_file, pdf_file)
        print("PDF created successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    html_file = "pdf_1.html"  # Path to your HTML file
    pdf_file = "output.pdf"   # Path to output PDF file
    html_to_pdf(html_file, pdf_file)
