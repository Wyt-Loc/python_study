# 字典的定义 值 和 键 的关系 字典写法{}

# 列表[] 元组()  字典{}

# 创建空字典
dictionary = {"key1": [1, 2, 3], "key2": [4, 5, 6]}
dictionary1 = {"key1": "1", "key2": "2"}
dictionary2 = dict()
print(dictionary)
print(dictionary1)
print(dictionary2)

# 通过映射函数创造字典
key = ["key1", "key2", "key3", "key4"]
value = [1, 2, 3, 4]
print(dict(zip(key, value)))

# 通过给定关键字参数创建字典
dictionary3 = dict(key1=1, key2=2, key3=3)
print(dictionary3)

# 通过fromkeys()方法创建字典  创建的只是键值为空的字典
dictionary4 = dict.fromkeys(value)
print(dictionary4)
KeyTuple = ("key1", "key2", "key3", "key4")
ValueList = [1, 2, 3, 4]
dictionary5 = {KeyTuple: ValueList}
print(dictionary5)

# 遍历字典 items()获取字典的所有键值对
print("遍历键值对")
for item in dictionary3.items():
    print(item)
for key, value in dictionary3.items():
    print(str(key), " 的值为 ", str(value))
