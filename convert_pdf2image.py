import pdf2image

file_name = "file_original/VA_Garnishment"

# Get the path to the PDF file
pdf_path = file_name + ".pdf"

# Convert the PDF to images
images = pdf2image.convert_from_path(pdf_path, dpi=300)

# Save the PNG images
for image in images:
    image.save(file_name + ".png")
