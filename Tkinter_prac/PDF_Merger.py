import os
from PyPDF2 import PdfFileMerger

source = r"C:\Users\M K DE\Desktop\Semester V\MPMC\Practical\Assignment_pdfs"

merger = PdfFileMerger()

for item in os.listdir(source):
    if item.endswith(".pdf"):
        result = source + r'/' + str(item)
        merger.append(result)

merger.write("118CS0163.pdf")
merger.close()
