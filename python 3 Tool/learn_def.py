'''
Python3 函数
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
函数能提高应用的模块性，和代码的重复利用率。
你已经知道Python提供了许多内建函数，比如print()。
但你也可以自己创建函数，这被叫做用户自定义函数。

语法：
def 函数名（参数列表）:
    函数体

'''

# 参数
'''
以下是调用函数时可使用的正式参数类型：

1.必需参数
2.关键字参数
3.默认参数
4.不定长参数
'''

# 必需参数
def showInfo(str):
	"打印任何字符串"
	print(str)

# 调用showInfo，必须传参
showInfo("调用showInfo，必须传参")


# 关键字参数
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致
def showInfo(name, age):
	"打印任何字符串"
	print(f"name = {name}")
	print(f"age = {age}")

showInfo(age = 29, name = "wzz")

# 默认参数 如果没有传递参数，则会使用默认参数
def showInfo(name = "wzz", age = 29):
	"打印任何字符串"
	print(f"name = {name}")
	print(f"age = {age}")

showInfo()


print("------不定长参数------")
# 不定长参数
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
def showInfo(name, *vartuple):
	"打印任何字符串"
	print(f"name = {name}")
	print(vartuple)

showInfo("wzz")
showInfo("wzz", 1, 2, 3)

# 加了两个星号 ** 的参数会以字典的形式导入
def showInfo(name = "wzz", **dict):
	"打印任何字符串"
	print(f"name = {name}")
	print(dict)

showInfo("wzz", id = 1991, age = 29)

print("----参数中星号 * 可以单独出现----")
# 参数中星号 * 可以单独出现
def showInfo(a, *, b):
	"打印任何字符串"
	print(a)
	print(b)
showInfo(1, b=3)


# 匿名函数 lambda
'''
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
'''
print("----lambda----")
sum = lambda a, b : a + b
print(f"sum(1, 2) = {sum(1, 2)}")

