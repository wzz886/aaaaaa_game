# 集合（set）是一个无序的不重复元素序列。
# 可以使用大括号 { } 或者 set() 函数创建集合，
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

# 定义
set1 = {"wzz", "age", "is", 28, 29}
set2 = set(("wzz", "age", "is", 30))

# 类似列表推导式，同样集合支持集合推导式
set3 = {x for x in set1 if x not in set2}
print(set3)

# 添加元素 (如果元素已存在，则不进行任何操作)
set3.add(28)
print(set3)

# 添加元素
set3.update({28, 29, 30})
print(set3)

# 删除元素 (元素不存在，报错)
set3.remove(28)

# 删除元素 (元素不存在，不报错)
set3.discard(28)

# 随机删除一个元素
print(set3.pop(), set3)

# 清空集合
# set3.clear()

# 判断元素是否在集合中存在
if 30 in set3:
	print(f"30 in set3 = {set3}")

'''
add()			为集合添加元素
clear()			移除集合中的所有元素
copy()			拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()			删除集合中指定的元素
intersection()		返回集合的交集
intersection_update()	返回集合的交集。
isdisjoint()		判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()		判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()			随机移除元素
remove()		移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()		返回两个集合的并集
update()	给集合添加元素

'''



