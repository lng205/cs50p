# Lec 6

文件读写。

- 使用with语法打开并关闭文件：

    ```Py
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            students.append({"name": name, "house": house})
    ```

- 使用匿名函数以及将函数作为参数：

    ```Py
    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['house']}")
    ```

- 将CSV文件首行作为表头，将每行存为一个表头-值字典，再把所有行放进一个列表，可实现表格结构

- 使用CSV库：

    ```Py
    import csv

    students = []

    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['home']}")
    ```

- 使用PIL库对二进制图片文件进行操作，将两张GIF合并为动图：

    ```Py
    import sys

    from PIL import Image

    images = []

    for arg in sys.argv[1:]:
        image = Image.open(arg)
        images.append(image)

    images[0].save(
        "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
    )
    ```

- 由于早期设计文件系统时，将文件建模为磁带式的顺序读写而非随机读写，因此目前习惯上仍对文件采用顺序读取，处理后再顺序写入的方式进行操作

## Problem Set 6

- 注意pizza题中tabulate库对字典列表表头参数的要求

- 羡慕网速
    ![网速](image.png)

- scourgify题，名是first name，姓是last name