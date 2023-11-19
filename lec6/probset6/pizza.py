from tabulate import tabulate
import sys, csv

if len(sys.argv) != 2:
    sys.exit("USAGE: python pizza.py FILE.csv")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File not found: " + sys.argv[1])

reader = csv.DictReader(file)
rows = []
for row in reader:
    rows.append(row)
file.close()

print(tabulate(rows, headers="keys", tablefmt="grid"))
