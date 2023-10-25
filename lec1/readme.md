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

## Problem Set 1

- 前两题在上一讲的基础上加入了条件判断，平滑过渡。
- 题目的背景均有一定的设计
- 第三题（extensions）需要查表提取信息，以及提取不定长后缀（该请鸭鸭助手登场了）
- meal有一个可选小挑战
