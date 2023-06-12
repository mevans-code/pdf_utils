import fitz

# Path of the PDF file
input_file = r"file_original/AI Impact.pdf"

# Path for the output PDF file
output_file = r"file_updated/AI Impact.pdf"

# Opening the PDF file and creating a handle for it
file_handle = fitz.open(input_file)

# The index (page no.) from where the pages are to be deleted
start = 4

# The index to which the pages are to be deleted
end = 7

# Passing the start & end index as arguments
file_handle.delete_pages(start, end)

# Saving the file
file_handle.save(output_file)
