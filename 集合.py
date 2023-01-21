# 使用赋值运算符直接创建集合
setname = {1, 2, 3, 1}  # 如果有重复的元素，只会保留一个
print(setname)

# 使用set()函数创建集合  set() 将列表 元组等转换为集合  转换字典好像只有键 没有值
dictionary = dict(key1=1, key2=2, key3=3)
set1 = set(dictionary)
print(set1)

List = [1, 2, 3]
Tuple = (1, 2, 3)
set2 = set(List)
print("set2为 " + str(set2))
set3 = set(Tuple)
print("set3为 " + str(set3))
