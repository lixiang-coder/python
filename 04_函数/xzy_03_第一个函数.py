name = "小明"


# 解释器知道这里定义了一个函数
def say_hello():
    """打招呼"""
    print("hello 1")
    print("hello 2")
    print("hello 3")


print(name)
# 只有在调用函数时，之前定义的函数才会被执行
# 函数执行完成之后，会重新回到之前的程序中，继续执行后续的代码
say_hello()

print(name)
