import re
import os
from pypdf import PdfReader


def extract_date_lines(pdf_path):
    """Extracts lines starting with a date in the format 'Mar 04' from all pages in a PDF.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        list: A list of strings, where each string represents a line starting with a date.
    """

    def get_full_date(date):
        return

    transaction_lines = []
    reader = PdfReader(pdf_path)

    for page in reader.pages:
        text = page.extract_text()  # Extract text using reliable method

        # Look for lines starting with a month followed by a space and two digits
        pattern = r"^(\b[ADFJMNOS][a-z]{2}\s+\d{2}.*)$"
        group_pattern = r"^(\b[ADFJMNOS][a-z]{2}\s+\d{2})(.*)(\s-?\d+\.\d{2})(.*)"
        matches = re.findall(group_pattern, text, re.MULTILINE)
        for match in matches:
            transaction = {
                "date": match[0],
                "type": match[1].strip(),  # Remove leading/trailing whitespace
                "amount": float(match[2]),
                "reference": match[3].strip(),
            }
            transaction_lines.append(transaction)

    return transaction_lines


if __name__ == "__main__":

    dir_path = "Statements"
    file_paths = ["Coles_17012024.pdf", "Coles_18022024.pdf", "Coles_17032024.pdf"]

    for path in file_paths:
        date_lines = extract_date_lines(os.path.join(dir_path, path))
        for line in date_lines:
            print(line)

