import csv 

with open('/chapter5/csv.csv') as f: 
    reader = csv.reader(f)
    for row in reader:
        print row
    