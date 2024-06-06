from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf():
    # Create a canvas (PDF document)
    c = canvas.Canvas("http_methods_explanation.pdf", pagesize=letter)

    # Set font and font size
    c.setFont("Helvetica", 12)

    # Add content to the PDF
    c.drawString(100, 750, "HTTP Methods: PUT and POST")

    c.drawString(100, 700, "PUT Method:")
    c.drawString(120, 680, "- Used to update an existing resource.")
    c.drawString(120, 660, "- Idempotent: Multiple identical requests have the same effect as a single request.")

    c.drawString(100, 620, "POST Method:")
    c.drawString(120, 600, "- to submit data to be processed to a specified resource.")
    c.drawString(120, 580, "- Typically used for creating new resources or actions that are not idempotent.")

    # Save the PDF
    c.save()
if __name__ == "__main__":
    create_pdf()

