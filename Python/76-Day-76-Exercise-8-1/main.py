# importing the necessary module
from PyPDF2 import PdfMerger

# creating an object of PDFMerger class
pdf_merger = PdfMerger()

# list of PDF files to merge
pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']

# merging PDF files
for pdf in pdf_files:
    with open(pdf, 'rb') as file:
        pdf_merger.append(file)

# write the merged PDF to a new file
with open('merged_file.pdf', 'wb') as file:
    pdf_merger.write(file)