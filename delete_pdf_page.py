import fitz

# Path of the PDF file
input_file = r"file_updated/AI Impact1.pdf"

# Path for the output PDF file
output_file = r"file_updated/AI Impact.pdf"

# Opening the PDF file and creating a handle for it
file_handle = fitz.open(input_file)

# The page no. denoted by the variable will be deleted
page = 0

# Passing the variable as an argument
file_handle.delete_page(page)

# Saving the file
file_handle.save(output_file)
