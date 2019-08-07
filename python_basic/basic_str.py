'''
字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。

'''
var1 = 'Hello World!'
var2 = "Runoob"

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

#-- r/R 原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。
print(r'\n')
print(R'\n')

#--   %s 格式化字符串;%d	 格式化整数
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

print("\n"+"="*50)
#-- 三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)
#-- capitalize()将字符串的第一个字母变成大写,其他字母变小写
str = "this is STRING example from runoob....wow!!!"

print ("str.capitalize() : ", str.capitalize())

print("\n"+"="*50)
#-- center 返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。
str = "[www.runoob.com]"

print ("str.center(40, '*') : ", str.center(40, '*'))

print("\n"+"="*50)
#-- count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。str.count(sub, start= 0,end=len(string))
str="www.runoob.com"
sub='o'
print ("str.count('o') : ", str.count(sub))

sub='run'
print ("str.count('run', 0, 10) : ", str.count(sub,0,10))

print("\n"+"="*50)
#-- encode decode
str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
print("GBK 解码：", str_gbk.decode('GBK', 'strict'))


print("\n"+"="*50)
#-- endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，否则返回 False。可选参数 "start" 与 "end" 为检索字符串的开始与结束位置。

Str='Runoob example....wow!!!'
suffix='!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix,20))
suffix='Run'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 3))


print("\n"+"="*50)
#-- find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。
str1 = "Runoob example....wow!!!"
str2 = "exam";

print("find: ",str1.find(str2))
print("find from 5: ",str1.find(str2, 5))
print("find from 10: ",str1.find(str2, 10))

print("\n"+"="*50)

print("\n"+"="*50)

print("\n"+"="*50)

print("\n"+"="*50)