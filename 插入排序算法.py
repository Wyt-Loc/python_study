# 插入排序


date = [58, 86, 29, 69, 10]


def insert(data: list):
    """
    @param data: 要排序的数据
    @return: 排序好的数据
    """
    for i in range(0, len(data)):
        temp = data[i]
        j = i - 1
        while j >= 0 and temp < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = temp

        print("第 %d 次排序结果为" % (i + 1), end=" ")
        for k in range(0, len(data)):
            print(data[k], end=" ")
        print()
    print("最终排序结果为 ")
    for i in range(len(data)):
        print(data[i], end=" ")
    print()
    return data


insert(date)
