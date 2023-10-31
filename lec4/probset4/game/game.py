from random import randint

def main():
    answer = randint(1, get_positive_int("Level: "))

    while True:
        guess = int(get_positive_int("Guess: "))
        if guess > answer:
            print("Too large!")
        elif guess < answer:
            print("Too small!")
        else:
            print("Just right!")
            break

def get_positive_int(prompt):
    while True:
        try:
            getted_int = int(input(prompt))
            if getted_int > 0:
                return getted_int
        except ValueError:
            pass

if __name__ == "__main__":
    main()
