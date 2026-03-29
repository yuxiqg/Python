# # Python 简易计算机

# operator = input("请输入运算符号(加法: + , 减法: - , 乘法: * , 除法: / ):")
# num1 = float(input("请输入第一个数字："))
# num2 = float(input("请输入第二个数字："))

# if operator == '+':
#     result = num1 + num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '/':
#     result = num1 / num2
# else:
#     print("运算符号无效")

# print(f"{num1} {operator} {num2} = {result}")

operator = input("请输入运算符号(加法: + , 减法: - , 乘法: * , 除法: / ):")

if operator == '+':
    num1 = float(input("请输入第一个加数："))
    num2 = float(input("请输入第二个加数："))
    result = num1 + num2
elif operator == '-':
    num1 = float(input("请输入被减数："))
    num2 = float(input("请输入减数："))
    result = num1 - num2
elif operator == '*':
    num1 = float(input("请输入第一个乘数："))
    num2 = float(input("请输入第二个乘数："))
    result = num1 * num2
elif operator == '/':
    num1 = float(input("请输入被除数："))
    num2 = float(input("请输入除数："))
    result = num1 / num2
else:
    print("请检查输入的运算符号是否正确")

print(f"{num1} {operator} {num2} = {result}")