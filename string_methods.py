# Python 的字串方法

# `len()` `find()` `index()`
# `capitalize()` `upper()` `lower()`
# `count()` `replace()`
# `isalpha()`

# help(str)  查询所有计算方法

# # 使用者的全名
# name = "sTrING String"

# # len() 计算一共有几个字符
# length = len(name)
# print("你的全名共有", length, "个字符")

# # find("") 找到第一个" "中的字符的位置，从0开始。如果没找到，返回 -1
# # index("") 找到第一个" "中的字符的位置，从0开始。如果没找到，抛出 ValueError 异常
# space_pos1 = name.find(" ")
# space_pos2 = name.index(" ")
# print("第一个空格出现在第", space_pos1, "个字符")
# print("第一个空格出现在第", space_pos2, "个字符")

# # capitalize() 首字母大写，其余全部小写
# name_capitalize = name.capitalize()
# print("你的全名（第一个字母大写）：", name_capitalize)

# # upper() 全部改为大写
# name_upper = name.upper()
# print("你的全名（全部大写）：", name_upper)

# # lower() 全部改为小写
# name_lower = name.lower()
# print("你的全名（全部小写）：", name_lower)

# # count("") 计算" "中的字符共有几个
# phone_number = input("请输入你的电话号码")
# dash_count = phone_number.count("-")
# print("你的电话号码中共有", dash_count, "个短横线")

# # replace("", "") 将第一个" "中的内容改成第二个" "中的内容
# phone_number = phone_number.replace("-", " ")
# print("你的电话号码（短横线换成空格）：", phone_number)

# # isalpha() 检查 字符串 是否 只包含字母
# username = input("请输入你的使用者名称")

# if username.isalpha():
#     print("全部是英文字符")
# else:
#     print("包含其他字符")


# 练习：验证使用者输入的合法性
# - 你的使用者名称不能超过 12 个字符
# - 你的使用者名称不能包含空格
# - 你的使用者名称不能包含数字
# - 如果都符合的话，显示 欢迎 + 使用者名称

username = input("请输入你的使用者名称")

count = username.count("0") + username.count("1") + username.count("2") + username.count("3") + username.count("4") + username.count("5") + username.count("6") + username.count("7") + username.count("8") + username.count("9")

if len(username) > 12:
    print("你的使用者名称不能超过 12 个字符")
elif " " in username: # 判断字符串中 是否 含有" "中的字符
    print("你的使用者名称不能包含空格")
elif not count == 0:
    print("你的使用者名称不能包含数字")
else:
    print("欢迎" + username) # print("" + string) 拼接字符串
