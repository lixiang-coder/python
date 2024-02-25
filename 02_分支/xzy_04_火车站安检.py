has_ticket = False
knife_length = 10.0

# 首先检查是否有车票
if has_ticket == 1:
# 如果有，再进行安检
    if knife_length >= 20:
        print("🔪的长度为：%0.2f，不允许上车" % knife_length)
    else:
        print("安检通过")
else:
    print("不允许进门")