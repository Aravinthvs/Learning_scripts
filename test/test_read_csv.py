import os
import csv

def read_csv(filename):
    # Get the directory of this test file
    base = os.path.dirname(__file__)
    
    # Build full file path
    filepath = os.path.join(base, filename)

    # Read CSV and return rows
    with open(filepath, "r") as f:
        return list(csv.DictReader(f))


def test_read_csv():
    data = read_csv("sample.csv")

    # Basic validations
    assert len(data) > 0
    assert "name" in data[0]      # check column