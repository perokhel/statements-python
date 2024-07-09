import csv

def filter_transactions_by_string(filenames, target_string, output_filename="target.csv"):
  """
  This function reads transactions from multiple CSV files, filters them based on a string in the
  description field, cleans extra spaces in the description, and writes the filtered transactions
  with cleaned descriptions to a new CSV file.

  Args:
      filenames: List of paths to CSV files containing transactions.
      target_string: String containing words to filter by (space separated).
      output_filename: Name of the output CSV file (default: target.csv).
  """
  # Split the target string into a list of words
  target_words = target_string.lower().split()

  filtered_transactions = []
  with open(output_filename, 'w', newline='') as target_file:
    writer = csv.writer(target_file)

    # Write header (assuming all files have the same header)
    writer.writerow(next(csv.reader(open(filenames[0]))))

    for filename in filenames:
      with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Skip header row (optional, adjust based on your CSV)
        next(reader, None)

        for row in reader:
          # Cleaned description with reduced spaces
          clean_description = " ".join(row[1].lower().split()).strip()

          # Check if all words in the target string are present in the cleaned description
          if all(word in clean_description for word in target_words):
            # Copy the row and replace description with cleaned version
            filtered_row = list(row)
            filtered_row[1] = clean_description
            filtered_transactions.append(filtered_row)

    # Write the filtered transactions with cleaned descriptions
    writer.writerows(filtered_transactions)


# Example usage
source_files = [".\\Statements\\trans080724-2.csv", ".\\Statements\\trans080724-1.csv"]
dest_file = ".\\Statements\\eppingautoservice.csv"
search_string = "epping auto serv"
filter_transactions_by_string(source_files, search_string, dest_file)
