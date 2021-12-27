# -*- coding: utf-8 -*-
# @Time : 2021/12/25 下午4:30 
# @Author : kimihiro
# @File : main.py 
# @Software: PyCharm
# Fibonacci数列的每后一项都是前面两项的和，若开始的头两项是1和2，那么前10个项就是：
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 请求出以上Fibonacci数列中不超过400,0000的所有偶数的和。

def main():
    a = 1
    b = 2
    final = 0
    while b < 4000000:
        if b % 2 == 0:
            final += b
        b = b + a
        a = b - a
    print(final)


if __name__ == '__main__':
    main()
