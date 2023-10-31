def main():
    sum = 0
    while True:
        coin = int(input("Insert Coin: "))

        # check coin
        if coin in [5, 10, 25]:
            sum += coin

        # check due
        due = 50 - sum
        if due <= 0:
            break

        # print due
        print(f"Amount Due: {due}")


    print(f"Change Owed: {-due}")

main()
