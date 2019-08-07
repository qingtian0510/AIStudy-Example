import copy

'''

什么是可变对象，什么是不可变对象：
可变对象是指，一个对象在不改变其所指向的地址的前提下，可以修改其所指向的地址中的值；
不可变对象是指，一个对象所指向的地址上值是不能修改的，如果你修改了这个对象的值，那么它指向的地址就改变了，相当于你把这个对象指向的值复制出来一份，然后做了修改后存到另一个地址上了，但是可变对象就不会做这样的动作，而是直接在对象所指的地址上把值给改变了，而这个对象依然指向这个地址。
    不可变数据（3个）：
    
    Number（数字）
    String（字符串）
    Tuple（元组）
    
    可变数据（3个）：
    
    List（列表）
    Dictionary（字典）
    Set（集合）


'''

'''
浅拷贝

1、对于 不可变类型 Number String Tuple,浅复制仅仅是地址指向，不会开辟新空间。
2、对于 可变类型 List、Dictionary、Set，浅复制会开辟新的空间地址(仅仅是最顶层开辟了新的空间，里层的元素地址还是一样的)，进行浅拷贝
3、浅拷贝后，改变原始对象中为可变类型的元素的值，会同时影响拷贝对象的；改变原始对象中为不可变类型的元素的值，只有原始类型受影响。 （操作拷贝对象对原始对象的也是同理）
'''

# 不可变类型 Number String Tuple
print("对于不可变类型 Number String Tuple,浅复制仅仅是地址指向，不会开辟新空间拷贝值")

num1 = 17
num2 = copy.copy(num1)

print("num1:" + str(id(num1)))
print("num2:" + str(id(num2)))
# num1和num2的地址都相同


str1 = "hello"
str2 = copy.copy(str1)
print("str1:" + str(id(str1)))
print("str2:" + str(id(str2)))
# str1和str2的地址都相同

tup1 = (18, "tom")
tup2 = copy.copy(tup1)
print("tup1:" + str(id(tup1)))
print("tup2:" + str(id(tup2)))
# tup1和tup2的地址都相同

print("="*20)
print("对于可变类型 List、Dictionary、Set，浅复制会开辟新的空间地址(仅仅是最顶层开辟了新的空间)，进行浅拷贝")


list1 = [11,12]
list2 = copy.copy(list1)
print("list1:" + str(id(list1)))
print("list2:" + str(id(list2)))
# list1和list2的地址不相同


dic1 = [11,12,"hi"]
dic2 = copy.copy(dic1)
print("dic1:" + str(id(dic1)))
print("dic2:" + str(id(dic2)))
# dic1和dic2的地址不相同

set1 = {"AA","BB"}
set2 = copy.copy(set1)
print("set1:" + str(id(set1)))
print("set2:" + str(id(set2)))
# set1和set2的地址不相同
print("\n")
print("="*50)
print("对list进浅拷贝，对可变类型和不可变类型修改后的影响。")
print("="*50)

'''
对list进浅拷贝，对可变类型和不可变类型修改后的影响。
'''
l1 = [11, 12]
l2 = [21, 22]
num = 555

allOne = [l1, l2,num]


# 浅拷贝，创建出一个对象，并把旧对象元素的 引用地址 拷贝到新对象当中。
# 也就是说，两个对象里面的元素通过浅拷贝指向的还是同一个地址
allOne2 = copy.copy(allOne)

l1[0] = 16 # 此处修改，会使得 allOne 和 allOne2的第0个元素的值都发生改变，因为l1是List，是可变对象
allOne[2] = 666 # 此处修改，只会allOne的num的值该改变，因为不可变对象一旦重新复制，地址就会发生改变。（不可变嘛）

num = 777 # 此处不会改变 allOne 和 allOne2的值，因为相当于 777 复制给一个全新的地址，这个num跟其他num已经没关系了

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

print("\n")
print("="*50)
print("对于不可变类型被修改后造成的影响。")
print("="*50)
num = 123
print(str(id(num)))

num = 666
print(str(id(num)))