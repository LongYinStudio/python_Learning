# 数据类型即数据的表现形式
# 常用的数据类型，type()函数返回数据的类型
# 1.字符串
a = 'I love you'
b = '我喜欢你'
c = "你好，世界！"
print(a, b, c)
print(type(a))  # <class 'str'>==string

# 2.数字类型 Number
num = 526  # 整型
print(num, type(num))
num1 = 6.1  # float浮点型
print(num1, type(num1))
num2 = 0x10  # 10进制
num3 = 1 + 8j  # complex复数
num4 = True  # bool布尔类型，取值只有True和False

# 3.列表[],可以储存任何数据类型，可修改
list0 = [1, "hello", True, 2.3, 1 + 7j]

# 4.元组(),可以储存任何数据类型，但不能修改
tuple0 = (1, "hello", True, 2.3, 1 + 7j)

# 5.集合{},可以储存任何数据类型，集合中元素无序且唯一（和高数的一样）
set0 = {1, "hello", True, 2.3, 1 + 7j}

# 6.字典{键(Key):值(Value)},键不能重复,和json相似
dict0 = {1: "这是1的值", "name": "这是name的值"}
print(dict0[1])

# 关于转义字符（常见的）
# \(在行尾时) 	续行符
# \\ 	反斜杠符号
# \' 	单引号
# \" 	双引号
# \a 	响铃
# \b 	退格(Backspace)
# \e 	转义
# \000 	空
# \n 	换行
# \v 	纵向制表符
# \t 	横向制表符
# \r 	回车
# \f 	换页
