# # Python 体重转换器

# weight = float(input("请输入你的体重："))
# unit = input("你的体重是公斤还是磅？(kg/lb)").upper() # .upper() 表示把字符转换成大写

# if unit == 'KG':
#     weight *= 2.2
#     new_unit = '磅'
# elif unit == 'LB':
#     weight /= 2.2
#     new_unit = '公斤'
# else:
#     print("单位不正确")
#     exit()

# print(f"你的体重是 {round(weight)} {new_unit}")


unit = input("你的体重是公斤还是磅？(kg/lb)").upper() # .upper 表示把字符变成大写

if unit == 'KG':
    weight = float(input("请输入你的体重："))
    weight *= 2.2
    new_unit = '磅'
elif unit == 'LB':
    weight = float(input("请输入你的体重："))
    weight /= 2.2
    new_unit = '公斤'
else:
    print("单位不正确")
    exit()

print(f"你的体重是 {round(weight)} {new_unit}")