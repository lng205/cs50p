# Lec 5

本节介绍单元测试。Python较高的开发效率使测试的性价比得到提升。

- 断言（assert）语法声称一个布尔表达式为真，若发现为假，则抛出AssertionError
- 测试用例常命名为test_测试对象名
- pytest库可帮助测试。可将测试文件打包（package）进行测试
- 将函数的副作用（side effect）改为返回值可以使测试更方便