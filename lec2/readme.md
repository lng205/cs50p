# lec 2

介绍了**循环**，在前两讲的基础上添加新内容。反复强调通过**函数**进行抽象的思维方式和编程习惯。

- for循环可按序取列表中的元素（iterate）
- range函数跟列表切片同样**左闭右开**
- 用**下划线**表示未使用的循环变量（Pythonic）

    ```python
    for _ in range(3):
    print("meow")```

- 函数**返回值**不需要在函数名所在的行声明
- **字典**通过**键**索引**值**（key-value）。C中没有类似的数据类型，但可通过哈希表[实现](https://github.com/lng205/CS50x2022/tree/master/Week5)类似效果。
- for会对字典的**键**进行迭代

    ```python
    students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
    }
    for student in students:
        print(student, students[student])```

- 通过字典构成的列表来存储表格。列表的元素对应表格中每行的对象，是一个由**表头-值**对构成的字典
- **None**表示空值

    ```python
    students = [
        {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None},
    ]

    for student in students:
        print(student["name"], student["house"], student["patronus"], sep=", ")```

- 先定义**子函数**，搭建框架，再逐步实现细节

## Problem Set 2

- Python 推荐使用下划线命名（snake_case）而非驼峰命名（camelCase）