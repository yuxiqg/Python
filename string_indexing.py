# Python 字符串索引

credit_number = "1234-5678-9876-5432"

first_char = credit_number[0]
print("第一个字符：", first_char)

second_char = credit_number[1]
print("第二个字符：", second_char)

first_four = credit_number[0:4] # 从 [0] 开始 到 [3] 结束
print("前四个字符：", first_four)

last_one = credit_number[-1] # [-1] 倒数第一个
print("倒数第一个字符：", last_one)

last_two = credit_number[-2] # [-2] 倒数第二个
print("倒数第二个字符：", last_two)