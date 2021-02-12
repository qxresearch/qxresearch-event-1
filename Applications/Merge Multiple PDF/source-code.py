from PyPDF2 import PdfFileMerger
# Download the following library using pip.
import os
# The above library already in your library.

# Make a function of PyPDF2 a variable.
merger = PdfFileMerger()

# Run the for loop to scan through all the pdf files.
# If wanted you can also just put the names of files instead of scanning all the files.
for items in os.listdir():  # os.listdir mean that it will scan through all the files.
    # This is an endswith function to check the extension of the object.
    if items.endswith('.pdf'):
        # This will append/add all projects.
        merger.append(items)

# This will write the whole document/ add it together into a new pdf.
merger.write("Rename.pdf")   # The name can easily be changed.

merger.close()

# This project is edited by Atul Anand based upon python version 3.9.
# I can assure you that this project will properly work if you use the latest version of python.
# Check my version of this project and many other projects on github.com/AtulACleaver.
