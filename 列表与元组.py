# 列表的创建 可以加[] 也可以不加[]
number = 1, 2, 3, 4  # 如果要进行列表相加的操作 这块貌似要加上[] 才好使 最好加上[]
number1 = [1, 2, 3, 4]
title = "123", "234", "345", "567"
untitle = ["人生苦短", "我用Python"]
EmptyList = []  # 创建空列表

# 创建数值列表list()
NumberList = list(range(1, 21, 2))  # 1 到 20 步长为 2 的数值列表
print(NumberList)

# 输列表元素
print(number)
print(untitle[0], untitle[1])  # 下标从 0 开始的 谨记

# 列表的截取和切片
SliceList = list(range(1, 21, 1))
print(SliceList)
print(SliceList[0:21:2])  # 下标从 0 开始
# 随意举几个例子练习
print(SliceList[1:5:1])
print(SliceList[8:13:1])
print(SliceList[13:16:1])
print(SliceList[::])  # 遍历整个列表 直接 2 个冒号
print(SliceList[::2])  # 步长为2

# 列表的拼接  前提是 2 相同类型的列表才能相加
SplicingList = number1 + NumberList
print(SplicingList)

# 遍历列表
# for 循环版本 实现
for item in SplicingList:
    print(item)

# 利用for 和enumerate() 实现
for index, item in enumerate(SplicingList):
    print("索引为 " + str(index + 1) + "列表值为 " + str(item))

# 输出索引为偶数位置的数值
print("偶数位置")
for index, item in enumerate(SplicingList):
    if index % 2 == 0:
        print("索引为 " + str(index) + "列表值为 " + str(item))

# 列表排序 sort(listname,key,reverse)排序后改变自身 其中key可以是一个函数
# sorted() 将排序的结果赋值给一个新的列表
grade = [98, 99, 97, 11, 123, 123, 4234, 5556, 111]
SortList = sorted(grade)
print("sorted()方法 " + str(SortList))
print("原列表为 " + str(grade))
grade.sort(reverse=False)
print("升 序 " + str(grade))
grade.sort(reverse=True)
print("降 序 " + str(grade))

# 元组 创建元组与创建列表类似 只是把[]改成()

# 创建空元组
EmptyTuple = ()

# 创建数值元组
# 方法1 使用tuple()函数
EmptyTuple = tuple(range(1, 21, 1))

print("数值元组 " + str(EmptyTuple))

# 访问元组数据
print("使用切片方法访问 " + str(EmptyTuple[::]))

# 使用for循环访问
print("for循环方法访问元组数据", end=" ")
for item in EmptyTuple:
    print(str(item), end=" ")

# 元组和列表的区别 列表中的元素可以进行任意修改 而元组中的元素无法修改，除非将元组整体替换掉
