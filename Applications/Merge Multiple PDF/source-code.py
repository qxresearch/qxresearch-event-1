#I have designed a simple User-Interface (UI) using Tkinter. Hope this helps in some way. Reach me out if you have any questions. Thank you!
from tkinter import Tk, Label, Button, filedialog
from PyPDF4 import PdfFileMerger
import os

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        root.title("PDF Merger")
        
        self.label = Label(root, text="PDF Merger Application")
        self.label.pack()
        
        self.select_folder_button = Button(root, text="Select Folder", command=self.select_folder)
        self.select_folder_button.pack()
        
        self.merge_button = Button(root, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.pack()
        
        self.remove_button = Button(root, text="Remove Original PDFs", command=self.remove_pdfs)
        self.remove_button.pack()
        
        self.selected_folder = ""
        
    def select_folder(self):
        self.selected_folder = filedialog.askdirectory()
        self.label.config(text=f"Selected Folder: {self.selected_folder}")
        
    def merge_pdfs(self):
        if self.selected_folder:
            merger = PdfFileMerger()
            for items in os.listdir(self.selected_folder):
                if items.endswith('.pdf'):
                    merger.append(os.path.join(self.selected_folder, items))
            merger.write(os.path.join(self.selected_folder, "Final_pdf.pdf"))
            merger.close()
            self.label.config(text="PDFs Merged Successfully!")
        else:
            self.label.config(text="Please select a folder first.")
            
    def remove_pdfs(self):
        if self.selected_folder:
            for items in os.listdir(self.selected_folder):
                if items != 'Final_pdf.pdf' and items.endswith('.pdf'):
                    os.remove(os.path.join(self.selected_folder, items))
            self.label.config(text="Original PDFs Removed Successfully!")
        else:
            self.label.config(text="Please select a folder first.")

if __name__ == "__main__":
    root = Tk()
    app = PDFMergerApp(root)
    root.mainloop()
