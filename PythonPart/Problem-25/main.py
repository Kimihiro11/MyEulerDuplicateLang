# -*- coding: utf-8 -*-
# @Time : 2022/1/31 下午2:58 
# @Author : kimihiro
# @File : main.py 
# @Software: PyCharm
# Fibonacci数列的定义如下：
# Fn = Fn-1 + Fn-2，且F1 = 1, F2 = 1。
# 于是前12个Fibonacci数就是：
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# 第十二项F12，是第一个达到三位数的Fibonacci数。
# 第一个达到1000位的Fibonacci数又是多少呢？
from functools import lru_cache


@lru_cache(maxsize=None)
def fib(x: int):
    if x == 1 or x == 0:
        return 1
    return fib(x - 1) + fib(x - 2)


def main():
    n = 1
    while len(str(fib(n))) < 1000:
        n += 1
    print(n)
    print(fib(4782))


if __name__ == '__main__':
    main()
