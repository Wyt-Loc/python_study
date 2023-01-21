# 冒泡排序


date = [1, 312, 45, 56, 13, 423, 56, 67]


def bubble(data: list):
    """
    @param data: 要排序的数据
    @return: 排序好的数据
    """
    for i in range(1, len(data)):
        for j in range(0, len(data) - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        print("第 %d 次排序结果为" % i, end=" ")
        for k in range(0, len(data)):
            print(data[k], end=" ")
        print()
    print("最终排序结果为 ")
    for i in range(len(data)):
        print(data[i], end=" ")
    print()
    return data


bubble(date)
