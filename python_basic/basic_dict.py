#字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
#键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
#1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
dict_0 = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}

print("dict_0['Name']: ", dict_0['Name'])

# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
dict2 = {('Name'): 'Runoob', 'Age': 7}

print("dict2['Name']: ", dict2['Name'])



dict_1 = {'name': 'test',2:3,('tuple'):'tuple'}

#-- len type str
print(len(dict_1))
print(type(dict_1))
print(str(dict_1))

#-- fromkeys 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
dict_new =  dict.fromkeys(['a',3],3)
print(dict_new)

#-- keys() values() items()
print(dict_new.keys())
print(dict_new.values())
print(dict_new.items())


#-- dict  pop
key = 'abcde'

value = range(1, 6)
dict_new2 = dict(zip(key, value))
print(dict_new2)
v = dict_new2.pop('a')
print("v= ",v," dict_new2= ",dict_new2)

filter_key = 'cde'
dict_new3 = {k: v for k, v in dict_new2.items() if k in filter_key}
print(dict_new3)



