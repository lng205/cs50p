# Lec 1

- 条件语句（elif）
- 流程图
- and语句的串联（90 <= score <=100）
- 布尔值
- 基于Python特性的编程（Pythonic）
- match语句（类似switch）：

    ```python
    name = input("What's your name? ")

    match name: 
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")
    ```

    注意按位或运算符（|）在match语句中被用于表达多项匹配（类似or在布尔表达式中的作用）
