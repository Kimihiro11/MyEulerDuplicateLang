# -*- coding: utf-8 -*-
# @Time : 2021/12/25 下午4:30 
# @Author : kimihiro
# @File : main.py 
# @Software: PyCharm


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
