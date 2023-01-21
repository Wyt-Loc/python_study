# 类的定义
# 创建完一个类后，要为其创建__init__()方法
class Student:
    """
    学生类
    """

    _num = 1

    # self指的是类实例对象本身
    def __init__(self):  # 类似于构造函数 在实例化这个类的时候自动执行
        self._num = 1  # 单下划线（_）是只允许类本身和子类访问 不能使用form ** import ** 导入
        self._name = "亚索"


wildGoose = Student()  # 类的实例化
print(wildGoose._num)  # num前加上_就不能通过本方法去访问这个_num变量不是准确的访问方式
print(wildGoose._name)
