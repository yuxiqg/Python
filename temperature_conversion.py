# # Python 温度转换器

# unit = input("请输入当前的温度单位(摄氏 C, 华氏 F):").upper() # .upper() 表示把字符转换成大写
# temp = float(input("请输入温度："))

# if unit == 'C':
#     temp = 9 * temp / 5 + 32
#     new_unit = 'F'
# elif unit == 'F':
#     temp = (temp -32) * 5 / 9
#     new_unit = 'C'
# else:
#     print("请输入正确的温度单位！")
#     exit()

# print(f"当前的温度是 {round(temp, 1)} {new_unit}")


unit = input("请输入当前的温度单位(摄氏 C, 华氏 F):").upper() # .upper() 表示把字符转换成大写

if unit == 'C':
    temp = float(input("请输入温度："))
    temp = 9 * temp / 5 + 32
    new_unit = 'F'
elif unit == 'F':
    temp = float(input("请输入温度："))
    temp = (temp -32) * 5 / 9
    new_unit = 'C'
else:
    print("请输入正确的温度单位！")
    exit()

print(f"当前的温度是 {round(temp, 1)} {new_unit}")