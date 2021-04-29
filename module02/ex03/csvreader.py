import csv

with open("test.csv", 'r') as f:
    r = csv.reader(f)
    for row in r:
        print(row)