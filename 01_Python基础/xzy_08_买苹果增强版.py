"""
# 收银员输入苹果的价格
price_str = input("请输入苹果的价格：")
# 收银员输入苹果的重量
weight_str = input("请输入苹果的重量：")
# 计算输出付款金额

# 将类型转化为int
price = float(price_str)
weight = float(weight_str)

money = price * weight
# print(type(money))
print(money)
"""

# 改进版
price =  float(input("请输入苹果的价格："))
weight = float(input("请输入苹果的重量："))
money = price * weight
print("付款金额为：%f" % money)
