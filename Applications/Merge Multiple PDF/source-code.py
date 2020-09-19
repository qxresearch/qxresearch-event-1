from PyPDF2 import PdfFileMerger
import os 
#var = os.getcwd() For extracting from enother folder
merger = PdfFileMerger()
for items in os.listdir():
  if items.endswith('.pdf')
    merger.append(items)
merger.write("Final_pdf.pdf")
merger = PdfFileMerger()
fin = file(originalFile, 'rb')
merger.append(PdfFileReader(fin))
fin.close()
os.remove(originalFile)
merger.close()

