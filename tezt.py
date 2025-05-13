"""
===================================
---                             ---
Author:JunHong
Time:2025/5/10 15:18
Email:123@qq.com
---                             ---
===================================
"""
from random import random


def func():
    data = (f"{i}@{10000000000000000000000+i+1}@20240898#job\n" for i in range(10000000))
    print(type(data))
    #data1 = (f" {1000000 + i}@20240898#job\n" for i in range(1000000))
    with open('example.txt', 'w',encoding='utf-8') as file:
        for line in data:
            file.write(line)


if __name__ == "__main__":
    func()