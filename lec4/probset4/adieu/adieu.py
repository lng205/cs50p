from inflect import engine

names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print()
        break

print("Adieu, adieu, to " + engine().join(names))
