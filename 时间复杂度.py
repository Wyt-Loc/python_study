# 暴力破解 贼慢
def Brute_force_cracking():
    for a in range(0, 1000):
        for b in range(0, 1000):
            for c in range(0, 1000):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    print("a,b,c", a, b, c)


# 升级版基本上秒出了
def Upgraded():
    for a in range(0, 1000):
        for b in range(0, 1000):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print("a,b,c", a, b, c)


if __name__ == "__main__":
    clk = 720000000
    for x in range(1, 720000000):
        if (clk / x**2 * 2) <= 12800:
            print(x)
            break
    # Brute_force_cracking()
    # Upgraded()
