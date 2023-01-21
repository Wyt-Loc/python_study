def Hundred_dollar_buy_Hundred_chicken():
    i = 0  # 公鸡
    j = 0  # 母鸡
    k = 0  # 小鸡
    for i in range(1, 20):
        for j in range(1, 32):
            for k in range(3, 99, 3):
                if i + j + k == 100 and 5 * i + 3 * j + k / 3 == 100:
                    print("公鸡为" + str(i) + "母鸡为" + str(j) + "小鸡为" + str(k))


if __name__ == "__main__":
    Hundred_dollar_buy_Hundred_chicken()
