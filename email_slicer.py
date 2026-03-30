# Email 字符串分析

email = "helloworld@python.com"

index = email.index("@") # index() 在字串中查询第一个出现在" "中的字符的位置
print(index)
print(email[:index])   # [:7] == [0:7]
print(email[index+1:]) # [7:] 从第7个到最后一个 