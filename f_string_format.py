# Python f-string 的 字符串格式化

price_1 = 3.321
price_2 = -77
price_3 = 15.11

# # 小数点的精确度
# print(f"价格 1 为 {price_1:.2f}\n" # .2f 表示显示小数点后2位
#       f"价格 2 为 {price_2:.2f}\n"
#       f"价格 3 为 {price_3:.2f}")

# # 加上正负号
# print(f"价格 1 为 {price_1:+.2f}\n" # + 表示显示正负号
#       f"价格 2 为 {price_2:+.2f}\n"
#       f"价格 3 为 {price_3:+.2f}")

# # 对齐  左对齐：<  右对齐：>  居中对齐：^
# print(f"价格 1 为 {price_1:<10.2f}\n" # :10 表示预设10位
#       f"价格 2 为 {price_2:^10.2f}\n"
#       f"价格 3 为 {price_3:>10.2f}")

# 混合不同符号
print(f"价格 1 为 {price_1:>+10.2f}\n"
      f"价格 2 为 {price_2:>+10.2f}\n"
      f"价格 3 为 {price_3:>+10.2f}")