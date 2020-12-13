# 斐波纳契数列: 两个元素的总和确定了下一个数
a, b = 0, 1
c = 0
list1 = [0, 1]
while len(list1) < 10 :
	c = a + b
	list1.append(c)
	a = b
	b = c
print(list1)
