# 顺序结构
a = 521
b = 1314
c = int(input("请输入c的值\r\n"))
print("a + b + c = " + str(a + b + c) + "\r\n")


# 条件分支结构
# if
grade = int(input("请输入成绩\r\n"))
if grade >= 60:
    print("成绩是 " + str(grade) + " 成绩通过")
if grade < 60:
    print("成绩是 " + str(grade) + " 成绩不及格\r\n")

# if else
grade1 = int(input("请输入成绩\r\n"))
if grade1 >= 60:
    print("成绩是 " + str(grade1) + " 成绩通过")
else:
    print("成绩是 " + str(grade1) + " 成绩不及格\r\n")

# if elif else
grade2 = int(input("请输入成绩\r\n"))
if 90 <= grade2 < 100:
    print("成绩是 " + str(grade2) + " 优秀")
elif 70 <= grade2 < 89:
    print("成绩是 " + str(grade2) + " 良好")
elif 60 <= grade2 < 79:
    print("成绩是 " + str(grade2) + " 及格")
else:
    print("成绩是 " + str(grade2) + " 不及格")

# if 的嵌套  这块是怎么复杂怎么写
age = int(input("请输入年龄\r\n"))
if 0 < age <= 20:
    if age <= 13:
        print("您是儿童")
    elif 13 < age <= 20:
        print("您是青少年")
else:
    if age <= 65:
        print("您是成年人")
    else:
        print("您是老年人")

# 循环结构 for
# range函数用法:起始值 结束值 步长
i = 0
for i in range(0, 5):
    print("*")

# 循环的嵌套
# 99乘法表
i = 1
j = 1
print("----------99乘法表----------")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(i) + "*" + str(j) + "=" + str(i * j) + "\t", end="")
    print("")

# 跳转语句 break continue 只可用于for循环和while循环中
# break 直接中止循环continue 跳转到下一次循环中

# break 版本
while True:
    matial = input("请输入配料表")
    if matial == "quit":
        break
    else:
        print("配料为" + matial)


# continue版本
while True:
    matial1 = input("请输入配料表")
    if matial1 == "quit":
        continue
    else:
        print("配料为" + matial1)
