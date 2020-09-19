from PyPDF2 import PdfFileWriter, PdfFileReader
pdfwriter=PdfFileWriter()
pdf=PdfFileReader("1.pdf")
for page_num in range(pdf.numPages):
  pdfwriter.addPage(pdf.getPage(page_num))
passw="xiaowuc2"
pdfwriter.encrypt(passw)
with open('ho.pdf','wb') as f:
  pdfwriter.write(f)
  f.close()
