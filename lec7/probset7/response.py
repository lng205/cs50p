from validators import email

if email(input()):
    print("Valid")
else:
    print("Invalid")
