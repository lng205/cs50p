def main():
    d = {}
    while True:
        try:
            item = input().upper()
            d[item] += 1
        except KeyError:
            d[item] = 1
        except EOFError:
            d_list = list(d)
            d_list.sort()
            for item in d_list:
                print(d[item], item)
            break


main()
