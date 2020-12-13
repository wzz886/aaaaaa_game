# 控制
# pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句

if True:
	pass
else:
	pass

num = 0
while num < 2:
	num += 1
	print(num)
else:
	print("退出while")

# for循环可以遍历任何序列的项目
# break 用于跳出当前循环体
# continue 用于跳到下个循环开始
tuple1 = (1, 2, 3)
for x in tuple1:
	if x == 3:
		break
	print(x)
else:
	print("not in tuple1")


# 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:
for i in range(2, 8, 2):
	print(i, end = ",")

# 使用range创建一个列表
print(list(range(5)))
