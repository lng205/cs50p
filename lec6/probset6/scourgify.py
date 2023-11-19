import sys, csv

if len(sys.argv) != 3:
    sys.exit("USAGE: python scourgify.py before.csv after.csv")

try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Could not read " + sys.argv[1])

rows = []
reader = csv.DictReader(file)
for row in reader:
    last, first = row["name"].split(", ")
    rows.append({"first": first, "last": last, "house": row["house"]})
file.close()

with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
