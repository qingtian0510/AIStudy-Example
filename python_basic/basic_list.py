
#-- append extend range :
list1 = ['physics', 'chemistry', 1997, 2000]

list1.append('test')   #一次加入一个元素进序列
print("after append:",list1)

list1.extend(range(5))  #一次把一个list加入list
print("after extend:",list1)
print(list1[1:5])
print(list1[:5:2])

print("len:",len(list1))

#-- del
del list1[2]
#print(list1)

#--  + *
a = [1,2,3]+[4,5,6]
b = ['hi ']*4
# print(a)
# print(b)
c = [a,b]

#-- max()
print(max([[1,5],[2,3]]))#按照元素里面list的第一个元素的排列顺序，输出最大值（如果第一个元素相同，则比较第二个元素，输出最大值）据推理是按ascii码进行排序的

print(a[-2])

#-- 迭代
for x in [a]:print(x)

#-- list()
tupl = (1,2,3)
#print(list(tupl))

#-- count
print(b.count('hi '))  #统计元素在list中出现的次数

#-- insert
a.insert(2,7)
print(a)

#-- pop   pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
print(a.pop())
print(a)

#-- remove remove() 函数用于移除列表中某个值的第一个匹配项。
b.remove('hi ')
print(b)

#-- reverse() 函数用于反向列表中元素。
a.reverse()
print(a)

#-- sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
a.sort()
print(a)

#-- clear() 函数用于清空列表，类似于 del a[:]

#-- copy() 函数用于复制列表，类似于 a[:]。
copy_a = a.copy()

#-- sum
print(sum(a))

#-- id() 函数用于获取对象的内存地址。
print(id(a))