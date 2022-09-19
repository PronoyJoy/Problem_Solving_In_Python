import PyPDF2
files = PyPDF2.PdfFileReader('Pronoy_Kumar_Das.pdf')

print(files.documentInfo)
print(files.getNumPages())
print(files.getPage(1))
