import copy

'''
深拷贝
1、浅拷贝，除了顶层拷贝，还对子元素也进行了拷贝（本质上递归浅拷贝）
2、经过深拷贝后，原始对象和拷贝对象所有的子元素地址都是独立的了
3、可以用分片表达式进行深拷贝
4、字典的copy方法可以拷贝一个字典
'''

# 不可变类型 Number String Tuple
print("对于不可 变类型 Number String Tuple,深复制依然是地址指向，不会开辟新空间拷贝值")

num1 = 17
num2 = copy.deepcopy(num1) # 深拷贝

print("num1:" + str(id(num1)))
print("num2:" + str(id(num1)))
# num1和num2的地址都相同


str1 = "hello"
str2 = copy.deepcopy(str1)  # 深拷贝
print("str1:" + str(id(str1)))
print("str2:" + str(id(str2)))
# str1和str2的地址都相同

tup1 = (18, "tom")
tup2 = copy.deepcopy(tup1) # 深拷贝
print("tup1:" + str(id(tup1)))
print("tup2:" + str(id(tup2)))
# tup1和tup2的地址都相同

print("="*20)
print("对于可变类型 List、Dictionary、Set，深拷贝会开辟新的空间地址，进行拷贝")


list1 = [11,12]
list2 = copy.deepcopy(list1) # 深拷贝
print("list1:" + str(id(list1)))
print("list2:" + str(id(list2)))
# list1和list2的地址不相同


dic1 = [11,12,"hi"]
dic2 = copy.deepcopy(dic1) # 深拷贝
print("dic1:" + str(id(dic1)))
print("dic2:" + str(id(dic2)))
# dic1和dic2的地址不相同

set1 = {"AA","BB"}
set2 = copy.deepcopy(set1) # 深拷贝
print("set1:" + str(id(set1)))
print("set2:" + str(id(set2)))
# set1和set2的地址不相同

print("="*20)
print("深拷贝的会对子元素也进行拷贝")

l1 = [11, 12]
l2 = [21, 22]
num = 555

allOne = [l1, l2,num]


# 浅拷贝，除了顶层拷贝，还对子元素也进行了拷贝（本质上递归浅拷贝）
# 经过深拷贝后，原始对象和拷贝对象所有的元素地址都没有相同的了

allOne2 = copy.deepcopy(allOne) # copy.deepcopy 深拷贝

allOne[1] = [113,114]
allOne2[2] = [227,228]

print(allOne)
print(allOne2)

print("id allOne:"+str(id(allOne)))
print("id allOne[0]:"+str(id(allOne[0])))
print("id allOne[1]:"+str(id(allOne[1])))
print("id allOne[2]:"+str(id(allOne[2])))

print("===")
print("id allOne2:"+str(id(allOne2)))
print("id allOne2[0]:"+str(id(allOne2[0])))
print("id allOne2[1]:"+str(id(allOne2[1])))
print("id allOne2[2]:"+str(id(allOne2[2])))


'''
其他拷贝方式
除了copy模块的中的copy和deepcopy，还有其他自带的方式可实现拷贝。

1、分片表达式进行浅拷贝
2、字典的copy方法可以拷贝一个字典
'''
print('\n')
print("="*50)
print("其他拷贝方式")

print("="*20)
print("1、分片表达式进行浅拷贝")

l1 = [11, 12]
l2 = [21, 22]
num = 555

orgi = [l1, l2, num]

nList = orgi[:]

print("orgi:"+str(id(orgi)))
print("orgi[0]:"+str(id(orgi[0])))
print("orgi[1]:"+str(id(orgi[1])))
print("orgi[2]:"+str(id(orgi[2])))
print("*"*30)
print("nList:"+str(id(nList)))
print("nList[0]:"+str(id(nList[0])))
print("nList[1]:"+str(id(nList[1])))
print("nList[2]:"+str(id(nList[2])))

print("="*20)
print("2、字典的copy方法可以拷贝一个字典")
dic = {"key": "hello", "num": 18}

dic2 = dic.copy()

dic["key"] = "one"
dic2["key"] = "two"

print(dic)
print("dic:" + str(id(dic)))

print(dic2)
print("dic2:" + str(id(dic2)))


