# importing required classes
from pypdf import PdfReader

file_path = 'G:\\My Drive\\Hamid\\20244301945430648FinalITGO.pdf'
# creating a pdf reader object
reader = PdfReader(file_path)

# printing number of pages in pdf file
print(len(reader.pages))

# creating a page object

for page in reader.pages:
    # extracting text from page
    print(page.extract_text())
    break
