# 1. 打印 9 行小星星
row = 1

while row <= 9:
    col = 1

    while col <= row:
        # print("*", end="")
        print("%d * %d = %d" % (row, col, row * col), end="\t")
        col += 1

    print("")
    row += 1
