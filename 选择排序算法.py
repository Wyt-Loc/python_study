# 选择排序
# 从未排序的数据中找到最小或者最大的加入另一个队列中


date = [1, 312, 312, 44, 411, 2134, 125, 123, 67, 78, 645, 7888]


def Select_Sort(data, trend):
    """
    @param data: 要排序的数据
    @param trend: 排序的方向 递增或递减
    @return: 排序好的数据
    """
    for i in range(0, len(data) - 1):
        for j in range(i + 1, len(data)):
            if trend == 1:
                if data[i] < data[j]:  # 递减排序
                    data[i], data[j] = data[j], data[i]
            if trend == 2:
                if data[i] > data[j]:  # 递增排序
                    data[i], data[j] = data[j], data[i]
        print("第 %d 次排序结果为" % (i + 1), end=" ")
        for k in range(0, len(data)):
            print(data[k], end=" ")
        print()
    print("最终排序结果为 ")
    for i in range(len(data)):
        print(data[i], end=" ")
    print()
    return data


print("递减排序")
Select_Sort(date, 1)
print("递增排序")
Select_Sort(date, 2)
