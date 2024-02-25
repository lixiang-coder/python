# 计算 0 ~ 100 之间所有数字的累计求和结果
i = 1
count = 0
while i <= 100:
    count = count + i
    i = i + 1
print("0 ~ 100 之间所有数字的累计求和结果为：%d" % count)

# 计算 0 ~ 100 之间 所有 偶数 的累计求和结果
j = 1
count1 = 0
# 判断是偶数才可进行求和
while j <= 100:
    # 判断是不是偶数
    if j % 2 == 0:
        count1 = count1 + j
    # 处理计数器
    j = j + 1

print("0 ~ 100 之间所有 偶数 的累计求和结果：%d" % count1)


