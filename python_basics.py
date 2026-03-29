#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python基础语法示例文件
涵盖Python主要基础语法特性
"""

# ==================== 1. 变量和数据类型 ====================
print("=== 1. 变量和数据类型 ===")

# 基本数据类型
integer_var = 42  # 整数
float_var = 3.14  # 浮点数
string_var = "Hello, Python!"  # 字符串
boolean_var = True  # 布尔值
none_var = None  # 空值

print(f"整数: {integer_var}")
print(f"浮点数: {float_var}")
print(f"字符串: {string_var}")
print(f"布尔值: {boolean_var}")
print(f"空值: {none_var}")

# 复合数据类型
list_var = [1, 2, 3, "Python", True]  # 列表 - 可变序列
tuple_var = (1, 2, 3, "Python")  # 元组 - 不可变序列
dict_var = {"name": "Alice", "age": 25, "city": "Beijing"}  # 字典 - 键值对
set_var = {1, 2, 3, 3, 2}  # 集合 - 无序不重复元素

print(f"列表: {list_var}")
print(f"元组: {tuple_var}")
print(f"字典: {dict_var}")
print(f"集合: {set_var}")  # 输出: {1, 2, 3}，重复元素被去重

# ==================== 2. 运算符 ====================
print("\n=== 2. 运算符 ===")

# 算术运算符
a, b = 10, 3
print(f"加法: {a} + {b} = {a + b}")
print(f"减法: {a} - {b} = {a - b}")
print(f"乘法: {a} * {b} = {a * b}")
print(f"除法: {a} / {b} = {a / b}")
print(f"整除: {a} // {b} = {a // b}")
print(f"取余: {a} % {b} = {a % b}")
print(f"幂运算: {a} ** {b} = {a ** b}")

# 比较运算符
print(f"等于: {a} == {b} -> {a == b}")
print(f"不等于: {a} != {b} -> {a != b}")
print(f"大于: {a} > {b} -> {a > b}")
print(f"小于: {a} < {b} -> {a < b}")
print(f"大于等于: {a} >= {b} -> {a >= b}")
print(f"小于等于: {a} <= {b} -> {a <= b}")

# 逻辑运算符
x, y = True, False
print(f"逻辑与: {x} and {y} -> {x and y}")
print(f"逻辑或: {x} or {y} -> {x or y}")
print(f"逻辑非: not {x} -> {not x}")

# 赋值运算符
c = 5
c += 3  # 等价于 c = c + 3
print(f"+= 运算符: c = {c}")
c *= 2  # 等价于 c = c * 2
print(f"*= 运算符: c = {c}")

# ==================== 3. 控制流语句 ====================
print("\n=== 3. 控制流语句 ===")

# if-elif-else 语句
score = 85
print(f"分数: {score}")

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"等级: {grade}")

# for 循环
print("\nfor 循环示例:")
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"水果: {fruit}")

# 使用 range() 函数
print("\nrange() 函数示例:")
for i in range(5):  # 0 到 4
    print(f"i = {i}")

for i in range(2, 6):  # 2 到 5
    print(f"i = {i}")

for i in range(0, 10, 2):  # 0 到 9，步长为 2
    print(f"i = {i}")

# while 循环
print("\nwhile 循环示例:")
count = 0
while count < 3:
    print(f"计数: {count}")
    count += 1

# break 和 continue
print("\nbreak 和 continue 示例:")
for i in range(10):
    if i == 3:
        continue  # 跳过当前迭代
    if i == 7:
        break  # 终止循环
    print(f"i = {i}")

# ==================== 4. 函数 ====================
print("\n=== 4. 函数 ===")

# 定义函数
def greet(name):
    """简单的问候函数"""
    return f"Hello, {name}!"

# 调用函数
result = greet("Alice")
print(result)

# 带默认参数的函数
def power(base, exponent=2):
    """计算幂，默认指数为2"""
    return base ** exponent

print(f"2的3次方: {power(2, 3)}")
print(f"5的平方: {power(5)}")  # 使用默认参数

# 可变参数
def sum_all(*args):
    """计算所有参数的和"""
    total = 0
    for num in args:
        total += num
    return total

print(f"求和: {sum_all(1, 2, 3, 4, 5)}")

# 关键字参数
def print_info(**kwargs):
    """打印关键字参数"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Bob", age=30, city="Shanghai")

# 匿名函数 (lambda)
square = lambda x: x ** 2
print(f"lambda函数: 5的平方 = {square(5)}")

# ==================== 5. 字符串操作 ====================
print("\n=== 5. 字符串操作 ===")

text = "Python Programming"

# 字符串索引和切片
print(f"字符串: {text}")
print(f"第一个字符: {text[0]}")
print(f"最后一个字符: {text[-1]}")
print(f"切片 [0:6]: {text[0:6]}")
print(f"切片 [7:]: {text[7:]}")

# 字符串方法
print(f"大写: {text.upper()}")
print(f"小写: {text.lower()}")
print(f"首字母大写: {text.title()}")
print(f"替换: {text.replace('Python', 'Java')}")
print(f"分割: {text.split(' ')}")
print(f"查找 'Pro': 位置 {text.find('Pro')}")
print(f"是否以 'Py' 开头: {text.startswith('Py')}")
print(f"是否包含 'gram': {'gram' in text}")

# 字符串格式化
name = "Charlie"
age = 28
print(f"f-string: {name} is {age} years old")
print("format方法: {} is {} years old".format(name, age))
print("百分号格式化: %s is %d years old" % (name, age))

# ==================== 6. 列表操作 ====================
print("\n=== 6. 列表操作 ===")

numbers = [1, 2, 3, 4, 5]

# 列表方法
numbers.append(6)  # 添加元素
print(f"添加后: {numbers}")

numbers.insert(2, 99)  # 在索引2处插入
print(f"插入后: {numbers}")

numbers.remove(99)  # 删除元素
print(f"删除后: {numbers}")

popped = numbers.pop()  # 弹出最后一个元素
print(f"弹出: {popped}, 剩余: {numbers}")

numbers.reverse()  # 反转列表
print(f"反转后: {numbers}")

numbers.sort()  # 排序
print(f"排序后: {numbers}")

# 列表推导式
squares = [x ** 2 for x in range(1, 6)]
print(f"列表推导式: {squares}")

even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"带条件的列表推导式: {even_squares}")

# ==================== 7. 字典操作 ====================
print("\n=== 7. 字典操作 ===")

person = {"name": "David", "age": 35, "city": "Guangzhou"}

# 访问字典
print(f"姓名: {person['name']}")
print(f"年龄: {person.get('age')}")
print(f"职业: {person.get('job', '未设置')}")  # 使用默认值

# 修改字典
person["age"] = 36  # 修改值
person["job"] = "Engineer"  # 添加新键值对
print(f"修改后: {person}")

# 遍历字典
print("遍历字典:")
for key, value in person.items():
    print(f"  {key}: {value}")

# 字典推导式
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(f"字典推导式: {squares_dict}")

# ==================== 8. 集合操作 ====================
print("\n=== 8. 集合操作 ===")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"集合A: {set_a}")
print(f"集合B: {set_b}")
print(f"并集: {set_a | set_b}")
print(f"交集: {set_a & set_b}")
print(f"差集(A-B): {set_a - set_b}")
print(f"对称差集: {set_a ^ set_b}")

# 集合推导式
even_set = {x for x in range(10) if x % 2 == 0}
print(f"集合推导式: {even_set}")

# ==================== 9. 异常处理 ====================
print("\n=== 9. 异常处理 ===")

def safe_divide(a, b):
    """安全的除法函数"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("错误: 除数不能为零!")
        return None
    except TypeError:
        print("错误: 参数类型错误!")
        return None
    else:
        print("除法成功!")
        return result
    finally:
        print("除法操作完成。")

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")

# 自定义异常
class NegativeNumberError(Exception):
    """自定义异常: 负数错误"""
    pass

def check_positive(number):
    """检查数字是否为正数"""
    if number < 0:
        raise NegativeNumberError("数字不能为负数!")
    return True

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(f"捕获自定义异常: {e}")

# ==================== 10. 文件操作 ====================
print("\n=== 10. 文件操作 ===")

# 写入文件
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("这是第一行\n")
    f.write("这是第二行\n")
    f.write("Python基础语法示例\n")

print("文件写入完成")

# 读取文件
try:
    with open("example.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print("文件内容:")
        print(content)
except FileNotFoundError:
    print("文件不存在!")

# ==================== 11. 面向对象编程 ====================
print("\n=== 11. 面向对象编程 ===")

class Animal:
    """动物基类"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic animal sound"
    
    def __str__(self):
        return f"{self.name} ({self.species})"

class Dog(Animal):
    """狗类，继承自动物类"""
    
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        return "Woof! Woof!"
    
    def fetch(self, item):
        return f"{self.name} fetches the {item}"

# 创建对象
animal = Animal("Generic", "Unknown")
dog = Dog("Buddy", "Golden Retriever")

print(f"动物: {animal}")
print(f"动物叫声: {animal.make_sound()}")

print(f"狗: {dog}")
print(f"狗叫声: {dog.make_sound()}")
print(f"狗的技能: {dog.fetch('ball')}")

# ==================== 12. 模块和包 ====================
print("\n=== 12. 模块和包 ===")

# 导入内置模块
import math
import random
import datetime

print(f"π的值: {math.pi}")
print(f"平方根: {math.sqrt(16)}")
print(f"随机数: {random.randint(1, 100)}")
print(f"当前时间: {datetime.datetime.now()}")

# ==================== 13. 生成器和迭代器 ====================
print("\n=== 13. 生成器和迭代器 ===")

# 生成器函数
def countdown(n):
    """倒计时生成器"""
    while n > 0:
        yield n
        n -= 1

print("倒计时生成器:")
for num in countdown(5):
    print(f"  {num}")

# 生成器表达式
gen_exp = (x * 2 for x in range(5))
print("生成器表达式:")
for value in gen_exp:
    print(f"  {value}")

# ==================== 14. 装饰器 ====================
print("\n=== 14. 装饰器 ===")

def timer_decorator(func):
    """计时装饰器"""
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行时间: {end_time - start_time:.6f}秒")
        return result
    
    return wrapper

@timer_decorator
def slow_function():
    """模拟耗时函数"""
    import time
    time.sleep(0.5)
    return "完成"

print(f"装饰器示例: {slow_function()}")

# ==================== 15. 上下文管理器 ====================
print("\n=== 15. 上下文管理器 ===")

class Timer:
    """自定义上下文管理器"""
    
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"代码块执行时间: {self.end - self.start:.6f}秒")

with Timer():
    # 模拟耗时操作
    total = 0
    for i in range(1000000):
        total += i

print("\n=== Python基础语法示例完成 ===")
print("这个文件涵盖了Python的主要基础语法特性，包括:")
print("1. 变量和数据类型")
print("2. 运算符")
print("3. 控制流语句")
print("4. 函数")
print("5. 字符串操作")
print("6. 列表操作")
print("7. 字典操作")
print("8. 集合操作")
print("9. 异常处理")
print("10. 文件操作")
print("11. 面向对象编程")
print("12. 模块和包")
print("13. 生成器和迭代器")
print("14. 装饰器")
print("15. 上下文管理器")