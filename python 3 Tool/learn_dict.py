# 字典
# 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
# 值可以取任何数据类型

# 定义
dict1 = {"name":"wzz", 29:"年龄"}

# 访问字典
print(f"my name id {dict1['name']}, {dict1[29]} 是 29")

# 修改字典
dict1["name"] = "wzz01"
dict1["id"] = 1991

# 删除元素
del dict1["name"]

print(dict1)

# 清空字典
dict1.clear()

# 删除字典
del dict1

# 内置方法
'''
1	radiansdict.clear()		删除字典内所有元素
2	radiansdict.copy()		返回一个字典的浅复制
3	radiansdict.fromkeys()	创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	radiansdict.get(key, default=None)返回指定键的值，如果键不在字典中返回 default 设置的默认值
5	key in dict如果键在字典dict里返回true，否则返回false
6	radiansdict.items()		以列表返回可遍历的(键		, 值) 元组数组
7	radiansdict.keys()		返回一个迭代器，可以使用 list()来转换为列表
8	radiansdict.setdefault(key, default=None)和get()		类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	radiansdict.update(dict2)	把字典dict2的键/值对更新到dict里
10	radiansdict.values()		返回一个迭代器，可以使用 list()来转换为列表
11	pop(key[,default])			删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
12	popitem()		随机返回并删除字典中的最后一对键和值。
'''

print(type({1, 2}))
