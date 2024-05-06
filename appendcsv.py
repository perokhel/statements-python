# Import writer class from csv module
from csv import writer


# # List that we want to add as a new row
# List = [6, 'William', 5532, 1, 'UAE']

def write_to_csv(data):
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open('fbrlist2.csv', 'w', encoding="utf-8") as f_object:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object, lineterminator="\n")

        # Pass the list as an argument into
        # the writerow()
        writer_object.writerows(data)

        # Close the file object
        f_object.close()
