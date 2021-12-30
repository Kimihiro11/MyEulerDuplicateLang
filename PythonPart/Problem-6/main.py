# -*- coding: utf-8 -*-
# @Time : 2021/12/30 下午8:58 
# @Author : kimihiro
# @File : main.py 
# @Software: PyCharm

# 前十个正整数的平方和是：12 + 22 + ... + 102 = 385
# 前十个正整数的和的平方是：(1 + 2 + ... + 10)2 = 552 = 3025
# 因此前十个正整数的和的平方，与前十个正数整数的平方和，的差是2640。
# 现在请你求出前一百个正整数的和的平方与前一百个正整数的平方和的差。

def main():
    square_sum = 0
    for i in range(1, 101):
        square_sum += pow(i, 2)
    sum_square = pow(101 * 50, 2)
    result = sum_square - square_sum
    print(result)


if __name__ == '__main__':
    main()
