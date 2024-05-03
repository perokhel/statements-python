from PyPDF2 import PdfWriter, PdfReader

page = PdfReader('G:\\My Drive\\Hamid\\20244301945430648FinalITGO.pdf')
numPages = len(page.pages)

print(page.pages[0].extract_text())
print('document has %s pages.' % numPages)
