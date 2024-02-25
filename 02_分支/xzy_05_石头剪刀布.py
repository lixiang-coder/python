# 导入随机数
import random

# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
quan = int(input("请输入你要出的拳 石头（1）／剪刀（2）／布（3）："))
# 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
computer = random.randint(1, 3)
print("玩家选择的拳头是：%d，电脑出的拳头是：%d" % (quan, computer))

# 比较胜负
"""
1. 石头 胜 剪刀
2. 布   胜 石头
3. 剪刀 胜 布
"""
if ((quan == 1 and computer == 2)
        or (quan == 3 and computer == 1)
        or (quan == 2 and computer == 3)):
    print("玩家胜")
elif quan == computer:
    print("平局")
else:
    print("电脑胜")
