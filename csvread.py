import csv


def filter_transactions_by_string(filenames, target_string, output_filename):
    """
    This function reads transactions from multiple CSV files, filters them based on a string,
    and writes the filtered transactions to a new CSV file.

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
                    # Convert the row to lowercase for case-insensitive matching
                    transaction_text = " ".join(word.lower() for word in row).strip()

                    # Check if all words in the target string are present in the transaction text
                    if all(word in transaction_text for word in target_words):
                        filtered_transactions.append(row)

        # Write the filtered transactions to the output file
        writer.writerows(filtered_transactions)


# Example usage
source_files = [".\\Statements\\trans080724-2.csv", ".\\Statements\\trans080724-1.csv"]
dest_file = ".\\Statements\\target.csv"
search_string = "tyre auto"
filter_transactions_by_string(source_files, search_string, dest_file)
