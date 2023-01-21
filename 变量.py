martial = "乾坤大挪移"
no = number = 2048
print(type(number))
print(type(martial))  # 获取变量类型
print(id(no))
print(id(number))  # 获取变量地址

# tip = int(input("请输入文字"))
# print("你输入的文字是\r\n" + str(tip))  # 输出的变量中有字符串 有数值型 则要把数值型强制转换为字符型

a = 19
b = 6
print(a)
print(b)
print(a * b)
print(a if a > b else b)
print(a / b)  # 除法
print(a // b)  # 取除uu
print(a % b)  # 求余数

if 18 < a < 20:  # 可以用这种方式
    print(a)
