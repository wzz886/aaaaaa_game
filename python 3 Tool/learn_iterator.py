'''
迭代器
迭代是Python最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器
'''

# 创建迭代器
list1 = [1, 2, 3, 4]
it = iter(list1)
print(next(it))
print(next(it))

# 使用for语句进行遍历迭代器：
for x in it:
	print(x, end = ",")


# 使用next语句进行遍历迭代器：
# import sys
it = iter(list1)
while True:
	try:
		print(next(it))
	except StopIteration:
		print("stop next(it)")
		break
		# sys.exit()


'''
创建一个迭代器
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
类都有一个构造函数，Python 的构造函数为 __init__()
__iter__() 方法返回一个特殊的迭代器对象
__next__() 方法会返回下一个迭代器对象。
'''

# 创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
print("-----创建一个返回数字的迭代器-------")
class MyNumbers:
	def __iter__(self):
		self.index = 10
		return self
	def __next__(self):
		index = self.index
		self.index += 10
		return index

myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))

# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况
print("--------防止出现无限循环---------")
class MyNumbers:
	def __iter__(self):
		self.index = 10
		return self
	def __next__(self):
		if self.index <= 50:
			index = self.index
			self.index += 10
			return index
		else:
			raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
 
for x in myiter:
  print(x)


# 使用了 yield 的函数被称为生成器（generator）
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，
# 返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

print("------yield 使用-----")
# 以下实例使用 yield 实现斐波那契数列：
import sys
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()



