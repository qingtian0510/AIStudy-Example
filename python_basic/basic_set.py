'''
集合（set）是一个无序的不重复元素序列。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''

a = set('abracadabra')
print(a)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}  # 这里演示的是去重功能
print(basket)

print("\n"+"="*50)

#-- add  update(参数可以是列表，元组，字典等)
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print("after add:",thisset)
thisset.update({1,3})
thisset.update([1,4],[5,6])
print("after update:",thisset)

print("\n"+"="*50)
#-- remove   将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误
#-- discard  移除集合中的元素，且如果元素不存在，不会发生错误
#thisset.remove("TaoBao")
print(thisset)
thisset.discard("TaoBao")
print(thisset)

print("\n"+"="*50)
#-- pop  随机删除集合中的一个元素,然而在交互模式，pop 是删除集合的第一个元素（排序后的集合的第一个元素
print("pop key:",thisset.pop(),"after pop:",thisset)

print("\n"+"="*50)
#-- union() : <set> | <set> 方法返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次。
#-- difference() : <set> - <set>方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。原集合不变
#-- intersection() : <set> & <set> 方法用于返回两个或更多集合中都包含的元素，即交集。
#-- symmetric_difference() : <set> ^ <set>方法返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。
#-- difference_update() 方法用于移除两个集合中都存在的元素。difference_update() 方法与 difference() 方法的区别在于 difference() 方法返回一个移除相同元素的新集合，而 difference_update() 方法是直接在原来的集合中移除元素，没有返回值。
#-- symmetric_difference_update()
#-- intersection_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
w = {"google","green"}



z = x.difference(y)
y.difference_update(w)
print("difference_update:",y)

print("difference:",z,"origin set:",x)
print("\n"+"="*50)

#-- intersection_update() 方法用于获取两个或更多集合中都重叠的元素，即计算交集。intersection_update() 方法不同于 intersection() 方法，因为 intersection() 方法是返回一个新的集合，而 intersection_update() 方法是在原始的集合上移除不重叠的元素
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

z = x.intersection(y)

print("intersection:",z)
print("\n"+"="*50)
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

z = x.union(y)

print("union:",z)

print("\n"+"="*50)
#--  isdisjoint() 方法用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

print("isdisjoint:",x.isdisjoint(y))

print("\n"+"="*50)
#-- issubset() 判断指定集合是否为该方法参数集合的子集。
#-- issuperset() 判断该方法的参数集合是否为指定集合的子集
# x.issubset(y) = y.issuperset(x)
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)
w = y.issuperset(x)

print("issubset:",z,"issuperset:",w)

print("\n"+"="*50)
#-- pop 随机移除元素
#-- remove 移除指定元素
fruits = {"apple", "banana", "cherry"}
fruits.pop()
fruits.add("test")

print("pop:",fruits)
print("before remove:",fruits)
fruits.remove("test")
print("after remove:",fruits)


