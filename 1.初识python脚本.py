# 这是单行注释，注释即运行时会被解释器忽略的给开发者用于标记的文字
'''多行注释'''
"""多行注释"""
# python缩进，4个空格为一个缩进
# 变量，注意：变量不能以数字开头，一般以英文字母开头
# 命名规范：不用中文（虽然可以使用），不用关键字（如if elif end for等等）
a = 1  # 将数字1赋予a
b = a + 1

# 使用print()函数打印b
print(b)

# 第二种定义变量的方式
x, y = 1, 2
print(x, y)

# 附：变量数据的交换的两种方式
q, w = 5, 6
print("q是", q, "w是", w)
# 1.新定义一个变量来用于数据交换
e = q
q = w
w = e
print("现在", "q是", q, "w是", w)
# 2.用python定义变量的语法来实现
t, y = 7, 8
print("t是", t, "y是", y)
t, y = y, t
print("现在", "t是", t, "y是", y)
