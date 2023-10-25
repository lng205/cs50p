greet = input("Greeting: ").lstrip().lower()
if greet[0] == "h":
    # take greet[1,2,3,4], think about greet[:-1]
    if greet[1:5] == "ello":
        print("$0")
    else:
        print("$20")
else:
    print("$100")