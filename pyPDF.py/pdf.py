from PyPDF2 import PdfReader,PdfWriter
a= PdfReader("apply domicile.pdf")
b= a.pages[0]

# text extraction
text=b.extract_text()
print(text,"\n")

# metadata details
print(a.metadata)
meta=a.metadata
# print(meta.creator)

#number of pages
print("number of pages in pdf is- ",len(a.pages))

#image from pdf
count=0
for image in b.images:
    with open(str(count)+image.name, "wb" ) as fp:
        fp.write(image.data)
        count+=1


#encrypting pdf
writer = PdfWriter()

# Add all pages to the writer
for page in a.pages:
    writer.add_page(page)

# Add a password to the new PDF
writer.encrypt("1234")

# Save the new PDF to a file
with open("encrypted-pdf.pdf", "wb") as f:
    writer.write(f)

#decrypting pdf
# reader = PdfReader("encrypted-pdf.pdf")
# writer = PdfWriter()

# if reader.is_encrypted:
#     reader.decrypt("my-secret-password")

# # Add all pages to the writer
# for page in reader.pages:
#     writer.add_page(page)

# # Save the new PDF to a file
# with open("decrypted-pdf.pdf", "wb") as f:
#     writer.write(f)