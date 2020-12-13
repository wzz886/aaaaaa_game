'''
Python 元组
Python的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号 ( )，列表使用方括号 [ ]。
创建:只需要在括号中添加元素，并使用逗号隔开即可。
'''

# 创建元组
tup1 = (50,) #元组中只包含一个元素时，需要在元素后面添加逗号
tup2 = "a", "b", "c", "d"   #  不需要括号也可以

# 修改元组
# 元组中的元素值是不允许修改的

# tup1[0] = 0 #报错

# 创建新元组
print(tup1 + tup1)

# 删除元组
# 元组中的元素值是不允许删除的，但可删除整个元组
del tup1

'''
元组运算符
与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制
运算后会生成一个新的元组。

Python 					表达式				结果	描述
len((1, 2, 3))			3					计算元素个数
(1, 2) + (4, 5)			(1, 2, 4, 5)		连接
('Hi!',) * 3			('Hi!', 'Hi!')		复制
3 in (1, 2, 3)			True				元素是否存在
for x in (1, 2, 3): 
	print x,			1 2 3				迭代
'''
