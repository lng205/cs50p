import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

name = sys.argv[1]

if not name.endswith(".py"):
    sys.exit("Not a Python file")

try:
    count = 0
    with open(name, "r") as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                count += 1

    print(count)
except FileNotFoundError:
    sys.exit("File does not exist")
