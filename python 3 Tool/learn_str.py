# 字符串
var1 = "Hello"
#		12345
#使用方括号 [] 来截取字符串
#索引值以 0 为开始值，-1 为从末尾的开始位置。
print(var1[0])
print(var1[1:2] + "!")

'''
	转义字符 \
	\(在行尾时)	续行符
	\\	反斜杠符号
	\'	单引号
	\"	双引号
	\n	换行
	\r	回车
	\t	制表符
'''

'''
+	字符串连接	a + b 输出结果： HelloPython
*	重复输出字符串	a*2 输出结果：HelloHello
[]	通过索引获取字符串中字符	a[1] 输出结果 e
[ : ] 截取字符串中的一部分，遵循左闭右开原则，str[0:2] 是不包含第 3 个字符的。	a[1:4] 输出结果 ell
in	成员运算符 - 如果字符串中包含给定的字符返回 True	'H' in a 输出结果 True
not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	'M' not in a 输出结果 True
r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 

'''
str1 = '''
多行字符串
	也可以用"""
'''


#字符串格式化
print("--------字符串格式化----------")
print("按默认顺序 {} {}".format(1, 2))
print("指定位置 {1} {0}".format(1, 2))
print("设置参数 name={name} id={id}".format(name = "wzz", id = 2))

#通过字典设置参数
site = {"name":"wzz", "id":2}
print("字典设置参数 name={name} id={id}".format(**site))

#通过列表索引设置参数
my_list = ["wzz", 2]
print("列表索引设置参数 name={0[0]} id={0[1]}".format(my_list)) #前面“0”表示，参数第一个列表

#通过传入对象
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('通过传入对象 value 为: {0.value}'.format(my_value))  # "0" 是可选的,“.”是必须的

####### f-string python3.6之后新增的################
name = "wzz"
age = 29
print(f"my name is {name}, age is {age}, id is {site['id']}")
print(f"age add + 1 = {age + 1}")
###################################################

print("--------数字格式化----------")
print ("我叫 %s 今年 %d 岁!" % ('wzz', 29))
'''
数字			格式		输出			描述
3.1415926	{:.2f}	3.14		保留小数点后两位
3.1415926	{:+.2f}	+3.14		带符号保留小数点后两位
-1			{:+.2f}	-1.00		带符号保留小数点后两位
2.71828		{:.0f}	3			不带小数
5			{:0>2d}	05			数字补零 (填充左边, 宽度为2)
5			{:x<4d}	5xxx		数字补x (填充右边, 宽度为4)
10			{:x<4d}	10xx		数字补x (填充右边, 宽度为4)
1000000		{:,}	1,000,000	以逗号分隔的数字格式
0.25		{:.2%}	25.00%		百分比格式
1000000000	{:.2e}	1.00e+09	指数记法
13			{:>10d}	    13		右对齐 (默认, 宽度为10)
13			{:<10d}	13			左对齐 (宽度为10)
13			{:^10d}	  13		中间对齐 (宽度为10)

以下是进制	
11			'{:b}'.format(11) 1011
11			'{:d}'.format(11) 11
11			'{:o}'.format(11) 13
11			'{:x}'.format(11) b
11			'{:#x}'.format(11) 0xb
11			'{:#X}'.format(11) 0XB	

---------------------------------
^, <, > 分别是居中、左对齐、右对齐，后面带宽度， 
: 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。

+ 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格

b、d、o、x 分别是二进制、十进制、八进制、十六进制。

'''
print("{:+.2f}".format(3.14159))


# 字符串内建函数
'''
capitalize()										将字符串的第一个字符转换为大写
center(width, fillchar)								返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
count(str, beg= 0,end=len(string))					返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
bytes.decode(encoding="utf-8", errors="strict")		Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
encode(encoding='UTF-8',errors='strict')			以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
endswith(suffix, beg=0, end=len(string))			检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
expandtabs(tabsize=8)								把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
find(str, beg=0, end=len(string))					检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
index(str, beg=0, end=len(string))					跟find()方法一样，只不过如果str不在字符串中会报一个异常。
isalnum()			如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False
isalpha()			如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False
isdigit()			如果字符串只包含数字则返回 True 否则返回 False..
islower()			如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
isnumeric()			如果字符串中只包含数字字符，则返回 True，否则返回 False
isspace()			如果字符串中只包含空白，则返回 True，否则返回 False.
istitle()			如果字符串是标题化的(见 title())则返回 True，否则返回 False
isupper()			如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
join(seq)			以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
len(string)			返回字符串长度
ljust(width[, fillchar])	返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
lower()						转换字符串中所有大写字符为小写.
lstrip()					截掉字符串左边的空格或指定字符。
maketrans()					创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
max(str)					返回字符串 str 中最大的字母。
min(str)					返回字符串 str 中最小的字母。
replace(old, new [, max])					把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。
rfind(str, beg=0,end=len(string))			类似于 find()函数，不过是从右边开始查找.
rindex( str, beg=0, end=len(string))		类似于 index()，不过是从右边开始.
rjust(width,[, fillchar])					返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
rstrip()									删除字符串字符串末尾的空格.
split(str="", num=string.count(str))		以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
splitlines([keepends])			 			按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
startswith(substr, beg=0,end=len(string))	检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
strip([chars])								在字符串上执行 lstrip()和 rstrip()
swapcase()									将字符串中大写转换为小写，小写转换为大写
title()										返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
translate(table, deletechars="")			根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
upper()										转换字符串中的小写字母为大写
zfill (width)								返回长度为 width 的字符串，原字符串右对齐，前面填充0
isdecimal()									检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
'''
