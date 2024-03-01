# 一个函数里面又调用了另外一个函数，这就是函数嵌套调用
def test1():
    print("*" * 50)
    print("test 1")
    print("*" * 50)


def test2():
    print("-" * 50)
    print("test 2")

    test1()

    print("-" * 50)


test2()
