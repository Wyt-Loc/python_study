# 过滤危险字符函数


def filterchar(string):
    """
    :param string:  字符串
    """
    import re

    pattern = r"(黑客)|(抓包)|(监听)|(Trojan)"
    sub = re.sub(pattern, "@_@", string)
    print(sub)


# 函数的调用
string1 = "我是一个黑客，喜欢抓包和监听想看看Trojan"
filterchar(string1)
