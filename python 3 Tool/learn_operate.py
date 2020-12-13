
print("---------------运算符 开始--------------------------")
a = 31
b = 20
print("a = %d, b = %d" % (a, b))
# print("a + b =", a + b)
# print("a - b =", a - b)
# print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b) #取整除 - 向下取接近商的整数 // 得到的并不一定是整数类型的数，它与分母分子的数据类型有关系。
print("a % b =", a % b) #取模 - 返回除法的余数
print("2 ** 3 =", 2 ** 3) #幂 - 返回2的3次幂

print("字符串*数字:","a" * 10) #返回重复若干次的字符串
'''
比较运算符
	==	等于
	!=	不等于
	>	大于
	<	小于
	>=	大于等于
	<=	小于等于
'''

'''
赋值运算符
	=	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
	+=	加法赋值运算符	c += a 等效于 c = c + a
	-=	减法赋值运算符	c -= a 等效于 c = c - a
	*=	乘法赋值运算符	c *= a 等效于 c = c * a
	/=	除法赋值运算符	c /= a 等效于 c = c / a
	%=	取模赋值运算符	c %= a 等效于 c = c % a
	**=	幂赋值运算符	c **= a 等效于 c = c ** a
	//=	取整除赋值运算符	c //= a 等效于 c = c // a

	:=	海象运算符，可在表达式内部为变量赋值。Python3.8 版本新增运算符。
		在这个示例中，赋值表达式可以避免调用 len() 两次:
		if (n := len({1, 2})) > 10:
		    print(f"List is too long ({n} elements, expected <= 10)")
'''

'''
位运算符
位运算符是把数字看作二进制来进行计算的。

&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1
|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
^	按位异或运算符：当两对应的二进位相异时，结果为1
~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。
<<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。
>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数


下表中变量 a 为 60，b 为 13二进制格式如下：
a      = 0011 1100
b      = 0000 1101
-----------------
a&b    = 0000 1100
a|b    = 0011 1101
a^b    = 0011 0001
~a     = 1100 0011
a << 2 = 1111 0000
a >> 2 = 0000 1111
'''

'''
逻辑运算符
and	  x and y	布尔"与" - 如果 x 为 False，x and y 返回 x 的值，否则返回 y 的计算值。	(a and b) 返回 20。
or	  x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
not	  not x	    布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
'''
print("10 and 20 = ", 10 and 20)

# and 比 or 拥有更高优先级
print("5 or 10 and False = ", 5 or 10 and False)

'''
成员运算符
in	如果在指定的序列中找到值返回 True，否则返回 False。
not in
'''
print("-------成员运算符 in ----------")
print("2 in [1, 4] =", 2 in [1, 4])

'''
成员运算符
is	如果在指定的序列中找到值返回 True，否则返回 False。
not is

is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个
== 用于判断引用变量的值是否相等。

注： id() 函数用于获取对象内存地址
'''
print("-------成员运算符 is ----------")
a = 20
b = 20
print("a is b =", a is b)
print("id(a) is id(b)", id(a) is id(b), id(a), id(b))
print("id(a) == id(b)", id(a) == id(b))

print("---------------运算符 结束--------------------------")
