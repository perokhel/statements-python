# importing required classes
from pypdf import PdfReader
import re
import os
from pprint import pprint
from appendcsv import write_to_csv
from textread import get_missing_records


def find_missing_serial_no(records_list):
    sr_no = 1
    missing = []
    for record in records_list:
        if record[0] != sr_no:
            missing.append(sr_no)
            sr_no += 1
        sr_no += 1
    return missing


def pdf_to_csv():
    file_path = 'G:\\My Drive\\Hamid\\20244301945430648FinalITGO.pdf'
    # creating a pdf reader object
    reader = PdfReader(file_path)

    # printing number of pages in pdf file
    print(len(reader.pages))
    pattern = r"^\b(\d+)\s(\d{13})\s([\w\s\.]+\-\w+)"
    buffer = []
    buffer.extend(get_missing_records())

    # creating a page object
    for page_index, page in enumerate(reader.pages):
        page_text = page.extract_text()
        matches = re.findall(pattern, page_text, re.MULTILINE)
        buffer.extend(matches)
        if len(buffer) >= 2000:
            # write_to_csv(matches)
            print("Page: ", page_index)
            print("Records: ", len(buffer)+1)
            print(find_missing_serial_no(buffer))
            pprint(buffer[-1][1])
            break


if __name__ == "__main__":
    pdf_to_csv()
