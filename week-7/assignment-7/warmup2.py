
import csv
# Open ../data/students.csv using a with block and read it line by line 

with open('../data/students.csv', "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        #print(f"row {number}: {score}")
        print(row['name'] + ":", row['score'])