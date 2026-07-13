from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
import os, getpass

file = "1.pdf"

#Create or fix empty PDF
if not os.path.exists(file) or os.path.getsize(file) == 0:
    c = canvas.Canvas(file)
    c.drawString(100, 750, "Auto-created PDF content")
    c.save()

#Read and protect
reader = PdfReader(file)
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt(getpass.getpass("Enter password: "))

with open("protected.pdf", "wb") as f:
    writer.write(f)

print("PDF protected successfully")