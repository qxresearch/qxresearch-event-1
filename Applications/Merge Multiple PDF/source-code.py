from PyPDF4 import PdfFileMerger
import os 
#var = os.getcwd() For extracting from enother folder
merger = PdfFileMerger()
for items in os.listdir():
  if items.endswith('.pdf'):
    merger.append(items)
merger.write("Final_pdf.pdf")
merger.close()

for items in os.listdir():
  if items != ( 'Final_pdf.pdf') and items.endswith('.pdf'):
    os.remove(items)