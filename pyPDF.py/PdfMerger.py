from pypdf import PdfWriter,PdfMerger
merger=PdfWriter() #or we can use pdfMerger also instead of PdfWriter.
files=["apply domicile.pdf","Python_Complete_Notes.pdf"]
for pdf_files in  files:
    merger.append(pdf_files)
merger.write("domicle_Python.pdf")
merger.close()