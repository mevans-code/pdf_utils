'''
This code will compare the two PDF files and print out the differences between
them. The differences will be printed out one page at a time, with the old and
new text for each difference.

You can also use the diff.get_changes() method to get a list of all the
changes between the two PDF files. This list will contain a dictionary for
each change, with the following keys:

old: The old text
new: The new text
page_number: The page number of the change
column: The column number of the change
row: The row number of the change
You can use this list to do more complex comparisons of the two PDF files.
'''
import pdfplumber

# Get the paths to the PDF files
pdf1_path = "file_updated/AI Impact1.pdf"
pdf2_path = "file_updated/AI Impact.pdf"

# Open the PDF files
pdf1 = pdfplumber.open(pdf1_path)
pdf2 = pdfplumber.open(pdf2_path)

# Compare the PDF files
diff = pdf1.compare(pdf2)

# Print the differences
for page in diff:
    print("Page {}: ".format(page.page_number))
    for difference in page.diffs:
        print("{} -> {}".format(difference.old, difference.new))
