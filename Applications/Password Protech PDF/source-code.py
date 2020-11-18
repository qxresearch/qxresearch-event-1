#current password for ho.pdf is 1234
from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass
pdfwriter=PdfFileWriter()
pdf_file = input("Enter Filename: ")
pdf=PdfFileReader(pdf_file)
for page_num in range(pdf.numPages):
  pdfwriter.addPage(pdf.getPage(page_num))
passw=getpass.getpass(prompt='Enter Password: ')
pdfwriter.encrypt(passw)
with open('ho.pdf','wb') as f:
  pdfwriter.write(f)
  f.close()
