# importing required classes
from pypdf import PdfReader

# creating a pdf reader object
reader = PdfReader('Coles_17032024.pdf')

# printing number of pages in pdf file
print(len(reader.pages))

# creating a page object

for page in reader.pages:
    # extracting text from page
    print(page.extract_text())