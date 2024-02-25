# 在控制台连续输出五行 * 每一行星号的数量依次递增
row = 0
while row <= 5:
    print("*" * row)
    row += 1

print("-" * 50)

row = 1

while row <= 5:

    # 假设 python 没有提供字符串 * 操作
    # 在循环内部，再增加一个循环，实现每一行的 星星 打印
    col = 1

    while col <= row:
        print("*", end="")

        col += 1

    # 每一行星号输出完成后，再增加一个换行
    print("")

    row += 1
