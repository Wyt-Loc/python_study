# 合并排序算法


def merge_sort(data: list):
    """
    @param data: 传入列表
    @return: 返回排序好的数据 从大到小
    """

    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    result = []
    while left and right:
        if left[0] >= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    elif right:
        result += right

    return result


if __name__ == "__main__":
    data = [12, 32, 55, 1, 67, 89, 66]
    print(merge_sort(data))
