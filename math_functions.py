import math

# # 加减乘除
# apples = 3

# 加法
# apples = apples + 1
# print(apples)
# apples += 1
# print(apples)

# 减法
# apples = apples - 1
# print(apples)
# apples -= 1
# print(apples)

# 乘法
# apples = apples * 2
# print(apples)
# apples *= 2
# print(apples)

# 除法
# apples = apples / 3
# print(apples)
# apples /= 2
# print(apples)


# # 指数（平方, 三次方)
# apples = 3

# apples = apples ** 3
# print(apples)
# apples **= 2
# print(apples)


# # 模除 mod

# # 10 mod 3 等于 3 余 1
# print(10 % 3)
# # 11 mod 3 等于 3 余 2
# print(11 % 3)
# # 12 mod 3 等于 4 余 0
# print(12 % 3)


# # 次方 pow()
# print(pow(2, 5)) # 2 的 5 次方
# print(pow(3, 2)) # 3 的 2 次方


# # 最大值 Max 与 最小值 Min
# x = 1
# y = 2
# z = 3
# print(max(x, y, z))
# print(min(x, y, z))


# # 四舍五入 round()
# a = 3.147
# print(round(a))
# print(round(a, 2)) # 保留 2 位小数的四舍五入
# b = 3.5
# print(round(b))


# # 绝对值 abs()
# c = -4
# print("绝对值:", abs(c))


# # 四舍五入、无条件进位、无条件舍去
# x = 9.5
# print(round(x))      # 四舍五入
# print(math.ceil(x))  # 无条件进位
# print(math.floor(x)) # 无条件舍去


# # 圆周率 pi
# print(math.pi)


# # 计算圆的周长
# radius = float(input("请输入圆的半径："))
# c = 2 * math.pi * radius
# print(f"圆的周长为：{round(c, 2)}")


# # 计算圆的面积
# radius = float(input("请输入圆的半径："))
# s = math.pi * pow(radius, 2)
# print(f"圆的面积是：{round(s, 2)}")