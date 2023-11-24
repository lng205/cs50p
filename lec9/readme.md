# Lec 9

本节是各种相关知识的补充。

- 集合（set）类型会自动去除重复数据

- Python函数可以直接读取全局变量，但需通过global关键字声明后，才能写入全局变量

- Type Hint可以标识变量类型，并通过mypy等程序检查：

    ```Py
    def meow(n: int):
        for _ in range(n):
            print("meow")


    number: int = input("Number: ")
    meow(number)
    ```

- 使用三个引号实现多行注释，通常用于函数的说明（docstring）。特定格式的说明可以直接被第三方工具转换为程序的说明文档：

    ```Py
    def meow(n):
        """
        Meow n times.

        :param n: Number of times to meow
        :type n: int
        :raise TypeError: If n is not an int
        :return: A string of n meows, one per line
        :rtype: str
        """
        return "meow\n" * n


    number = int(input("Number: "))
    meows = meow(number)
    print(meows, end="")
    ```

- 方括号内的参数在说明文档中通常表示可选项

- argparse库可以处理命令行参数：

    ```Py
    import argparse

    parser = argparse.ArgumentParser(description="Meow like a cat")
    parser.add_argument("-n", default=1, help="number of times to meow", type=int)
    args = parser.parse_args()

    for _ in range(args.n):
        print("meow")
    ```

- "*"可以对列表这样的序列进行解包（Unpack），实现类似对多个变量同时赋值的效果。"**"可以对字典解包，作为关键字参数传入函数：

    ```Py
    def total(galleons, sickles, knuts):
        return (galleons * 17 + sickles) * 29 + knuts


    coins = [100, 50, 25]

    print(total(*coins), "Knuts")
    ```

    ```Py
    def total(galleons, sickles, knuts):
        return (galleons * 17 + sickles) * 29 + knuts


    coins = {"galleons": 100, "sickles": 50, "knuts": 25}

    print(total(**coins), "Knuts")
    ```

- "*"和"**"在函数的参数中分别表示任意数量的位置参数和关键字参数，传入的参数会存储为元组（Tuple）和字典：

    ```Py
    def f(*args, **kwargs):
        print("Named:", kwargs)


    f(galleons=100, sickles=50, knuts=25)
    ```

- map函数可以对一个可迭代对象逐个应用函数并返回

    ```Py
    def main():
        yell("This", "is", "CS50")


    def yell(*words):
        uppercased = map(str.upper, words)
        print(*uppercased)


    if __name__ == "__main__":
        main()
    ```

- List Comprehension可以直接从可迭代对象生成一个列表，等价于对一个空列表不断append：

    ```Py
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
    ]

    gryffindors = [
        student["name"] for student in students if student["house"] == "Gryffindor"
    ]

    for gryffindor in sorted(gryffindors):
        print(gryffindor)
    ```

- Dictionary Comprehension：

    ```Py
    students = ["Hermione", "Harry", "Ron"]

    gryffindors = {student: "Gryffindor" for student in students}

    print(gryffindors)
    ```

- filter函数与map一样接受一个函数和一个可迭代对象作为参数，若将迭代元素传入函数得到的返回值为真，则将元素加入filter函数传回的列表中

- enumerate函数可以对列表迭代，同时返回序号和元素

- generator在函数中使用yield语法返回，使函数可以在多次调用时保持内部状态，成为一个可迭代对象

![Alt text](image.png)