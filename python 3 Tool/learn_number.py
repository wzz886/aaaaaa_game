'''
Python 支持三种不同的数值类型：
数据类型是不允许改变的,这就意味着如果改变数字数据类型的值，将重新分配内存空间。

int     整型，  没有限制大小
float   浮点型, 整数部分与小数部分组成
complex 复数,   由实数部分和虚数部分构成，
			    可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

'''
print("----数值类型----")
print(type(1))
print(type(1.2))
print(type(1.2j))

'''
Python 数字类型转换,将数据类型作为函数名即可。
int(x) 将x转换为一个整数。
float(x) 将x转换到一个浮点数。
complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。
'''

print("----------数学函数--------")

# abs(x)	返回数字的绝对值，如abs(-10) 返回 10
# cmp(x, y) 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 
#           Python 3 已废弃，使用 (x>y)-(x<y) 替换。(int(False) = 0, int(True) = 1)
# max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
# min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
# pow(x, y)	x**y 运算后的值。
# round(x [,n])返回浮点数 x 的四舍五入值， n位小数点后的位数。

#以下需要导入math，使用时，前面要加math
#import math
# ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
# modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
# exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
# fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
# floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
# log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
# log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0	
# sqrt(x)	返回数字x的平方根。

# 三角函数
# acos(x)	返回x的反余弦弧度值。
# asin(x)	返回x的反正弦弧度值。
# atan(x)	返回x的反正切弧度值。
# atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
# cos(x)	返回x的弧度的余弦值。
# hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
# sin(x)	返回的x弧度的正弦值。
# tan(x)	返回x弧度的正切值。
# degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
# radians(x)	将角度转换为弧度

#import random
# 随机数函数
# choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
# randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
# random()	随机生成下一个实数，它在[0,1)范围内。
# seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
# shuffle(lst)	将序列的所有元素随机排序
# uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。

