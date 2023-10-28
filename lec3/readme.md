# Lec 3

本讲介绍了异常处理。全新内容，Python的独特而实用的特性。

- try语句

    ```python
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        print(f"x is {x}")```

- 针对具体的错误类型写异常处理
- 语法错误无法在运行时处理
- 用pass关键字跳过异常处理
- Python允许程序报错而不是必须提前检查，解释型语言的优势

## Shorts

介绍debug技巧。

- step over会运行完当前行，在下一行前停止
- step into会进入子函数，在子函数第一行前停止

## Problem Set 3

题目难度递增，第一题主要对课内介绍的概念进行运用，后面的题目逐步引入新内容。

- taquria问题介绍了多个新异常