# -*- coding: utf-8 -*-
# @Time : 2021/12/25 下午9:19 
# @Author : kimihiro
# @File : main.py 
# @Software: PyCharm
import copy


# 求由两个3位数相乘得到的最大的回文数。
def is_palindromic_number(number: int):
    r_li = []
    while number > 0.1:
        seat = number % 10
        r_li.append(seat)
        number = number // 10
    host = copy.copy(r_li)
    r_li.reverse()
    if host == r_li:
        return True


def main():
    l = []
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            s = i * j
            if is_palindromic_number(s):
                l.append(s)
    print(max(l))
    # for i in range(999, 100, -1):
    #     num_temp = i % 10 * 100 + (i // 10) % 10 * 10 + i // 100
    #     num = i * 1000 + num_temp
    #     for i in range(999, 100, -1):
    #         if num % i == 0:
    #             if num // i <= 999 and num // i >= 100:
    #                 print(i, num // i, num)
    #                 break
    #     else:
    #         continue
    #     break

if __name__ == '__main__':
    main()
