import csv


# This method opens the .csv file in reading mode, skips the header row, adds all other lines to the list of test data values test_data one by one and returns the test data object.
def read_test_data_from_csv():
    test_data = []
    with open("test_data/gorest_post_rqst_data.csv", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        next(data)  # skip header row
        for row in data:
            test_data.append(row)
    return test_data
