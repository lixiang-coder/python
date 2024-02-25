# 练习1: 定义一个整数变量 `age`，编写代码判断年龄是否在0-120之间
age = 20

if age >= 0 and age <= 120:
    print("正确")
else:
    print("错误")

#  练习2: 定义两个整数变量 `python_score`、`c_score`，编写代码判断成绩
python_score = 61
c_score = 59

if python_score > 60 or c_score > 60:
    print("合格")
else:
    print("不合格")

# 练习3: 定义一个布尔型变量 `is_employee`，编写代码判断是否是本公司员工
is_employee = False
if is_employee == 1:
    print("允许入内")
else:
    print("禁止入内")