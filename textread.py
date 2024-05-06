import re
from pprint import pprint


def get_missing_records(txt_path='fbrfirstpage.txt'):
    text_pattern = r"^\b(\d+)\s(\d{13})\s(.+)$"
    with open(txt_path, 'r') as text_file:
        text_matches = re.findall(text_pattern, text_file.read(), re.MULTILINE)
        return text_matches


if __name__ == "__main__":
    pprint(get_missing_records())
