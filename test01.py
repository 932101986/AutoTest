"""
===================================
---                             ---
Author:JunHong
Time:2024/11/21 22:03
Email:123@qq.com
---                             ---
===================================
"""


class Stranger(object):
    def __init__(self, gender=None, age=None, job=None):
        self.gender = gender
        self._age = age  # 这里的成员属性_age需要与成员方法age()区分开
        self.jobb = job

    # 读取age
    @property  # 实现一个age相关的getter方法
    def age(self):
        return self._age

    # 设置age
    @age.setter  # 实现一个age相关的setter方法
    def age(self, value):
        if isinstance(value, int):
            self._age = value
        else:
            raise ValueError("'int' type need")


if __name__ == "__main__":
    # 创建一个“妹子”
    meizi = Stranger()

    meizi.age = 18  # 使用时注意是.age，不是._age

    print("年龄:{age}".format(age=meizi.age))
    dict1={'name':"嘻哈",'age':90}
    for key in dict1:
        print(key)