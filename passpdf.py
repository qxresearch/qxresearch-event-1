from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass

# Making an instance of the PdfFileWriter class and storing it in a variable
writer = PdfFileWriter()


# Explicitly ask the user what the name of the original file is
pdf_name = input('Pleast type in the name of the pdf file suffixed with its extention: ')

# Making an instance of the PdfFileReader class with the original file as an argument
original_file = PdfFileReader(pdf_name)

# Copies the content of the original file to the writer variable
for page in range(original_file.numPages):
    writer.addPage(original_file.getPage(page))

# Retrieve a preferred password from the user 
password = getpass.getpass(prompt = "Set a Password: ")

# Encrypt the copy of the original file
writer.encrypt(password)

# Opens a new pdf (write brinary permission) and writes the content of the 'writer' into it
with open('secured.pdf', 'wb') as f:
    writer.write(f)
    f.close()
