
# Python有6个序列的内置类型，但最常见的是列表和元组。
# 序列都可以进行的操作包括索引，切片，加，乘，检查成员。
# Python已经内置确定序列的长度以及确定最大和最小的元素的方法。

#列表 List

# 定义
list1 =[1, "wzz", 'learn']

# 访问列表中的值
print("list1[1]=", list1[1])
print("list1[1:3] =", list1[1:3]) #返回一个列表，包第二个和第三个元素

# 修改列表中的值
list1[0] = "999"

# 增加列表中的值
list1.append("py")

# 删除列表中的元素
del list1[0]
print(list1)

#列表脚本操作符
'''
Python表达式			结果				描述
len([1, 2, 3])		3				长度
[1, 2,] + [4, 5]	[1, 2, 4, 5]	组合
['Hi!'] * 2			['Hi!', 'Hi!']	重复
3 in [1, 2, 3]		True			元素是否存在于列表中
for x in [1, 2, 3]: 
	print x,		1 2 3			迭代
'''

#Python列表函数&方法
'''
序号	函数
1	cmp(list1, list2) 	比较两个列表的元素
2	len(list) 			列表元素个数
3	max(list)			返回列表元素最大值
4	min(list) 			返回列表元素最小值
5	list(seq) 			将元组转换为列表
'''

'''
Python包含以下方法:

序号	方法
1	list.append(obj)		在列表末尾添加新的对象
2	list.count(obj)			统计某个元素在列表中出现的次数
3	list.extend(seq)		在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)			从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)	将对象插入列表
6	list.pop([index=-1])	移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)		移除列表中某个值的第一个匹配项
8	list.reverse()			反向列表中元素
9	list.sort(cmp=None, key=None, reverse=False)对原列表进行排序
10	list.clear()			清空列表
11	list.copy()				复制列表

'''

