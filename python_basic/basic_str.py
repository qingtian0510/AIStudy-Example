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
#-- lower() 方法转换字符串中所有大写字符为小写。
#-- upper() 方法将字符串中的小写字母转为大写字母。
#-- swapcase() 方法用于对字符串的大小写字母进行转换。大写转成小些，小写转成大写
str = "this is STRING example from runoob....wow!!!"

print ("str.capitalize() : ", str.capitalize())
print ("str.lower() : ", str.lower())

print("\n"+"="*50)
#-- center 返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。
#-- ljust 返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串.
#-- rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。


str = "Runoob example....wow!!!"

print ("str.ljust(50, '*'):",str.ljust(50, '*'))
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
#-- startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。

Str='Runoob example....wow!!!'
suffix='!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix,20))
suffix='Run'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 3))


print("\n"+"="*50)
#-- find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。
#-- rfind() 返回字符串最后一次出现的位置，如果没有匹配项则返回-1。
#-- index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
#-- rindex() 返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间。
str1 = "Runoob example....wow!!!"
str2 = "exam";

print("find: ",str1.find(str2))
print("find from 5: ",str1.find(str2, 5))
print("find from 10: ",str1.find(str2, 10))

print("\n"+"="*50)
#-- format
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', '菜鸟教程']
my_list2 = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {1[1]}".format(my_list,my_list2))  # "{0[0]}" :{0}表示第一个参数，0[0]表示一个元素

print("\n"+"="*50)
#-- isalnum 如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
#-- isalpha 如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
#-- isdigit 如果字符串只包含数字则返回 True 否则返回 False。
str = "runoob2016"  # 字符串没有空格
print("isalnum:",str.isalnum())
str = "www.runoob.com"
print("isalnum:",str.isalnum())

str = "runoob"
print ("isalpha:",str.isalpha())
str = "Runoob example....wow!!!"
print ("isalpha:",str.isalpha())

str = "123456";
print ("isdigit:",str.isdigit())
str = "Runoob example....wow!!!"
print ("isdigit:",str.isdigit())

print("\n"+"="*50)
#-- join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print ("join:",s1.join( seq ))
print ("join:",s2.join( seq ))


print("\n"+"="*50)
#-- strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。
#-- lstrip() 方法用于截掉字符串左边的空格或指定字符。
#-- rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.

str = "     this is string example....wow!!!     ";
print("str.lstrip:",str.lstrip())
str = "88888888this is string example....wow!!!8888888";
print("str.lstrip:",str.lstrip('8'))
print("str.rstrip:",str.rstrip('8'))


print("\n"+"="*50)
#-- max 方法返回字符串中最大的字母。
#-- min 返回字符串中最小的字母。
str = "runoob";
print("最大的字符：",max(str))
print("最小的字符：",min(str))

print("\n"+"="*50)
#--  replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
str = "www.w3cschool.cc"
print("菜鸟教程旧地址：", str)
print("菜鸟教程新地址：", str.replace("w3cschool.cc", "runoob.com"))

str = "this is string example....wow!!!"
print(str.replace("is", "was", 3))

print("\n"+"="*50)
#-- split() 通过指定分隔符对字符串进行切片，如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。
#-- splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
txt = "Google#Runoob#Taobao#Facebook"

# 第二个参数为 1，返回两个参数列表
print("split once:",txt.split("#", 1))