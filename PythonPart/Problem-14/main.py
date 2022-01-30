# -*- coding: utf-8 -*-
# @Time : 2022/1/30 下午3:48 
# @Author : kimihiro
# @File : main.py 
# @Software: PyCharm

"""下面的循环数列是由正整数根据以下规则构成的：
n → n/2 (若n是偶数)
n → 3n + 1 (若n是奇数)
若数列从13开始，就生成了如下数列：
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
显然以上数列有10个数字，虽然未经证明（著名的Collatz猜想），但我们认为无论由什么数字开始，数列都会在1处结束。故数列一旦产生了1这一项，就认为数列结束。
这次的问题是：根据以上规则，由100万以下的哪个数字开始，可以产生最长的数列？
请注意：产生的数列可能会包含数字超过100万的项。"""
li = [0 for i in range(10000000)]


def calculate(num: int):
    if num == 1:
        return 1
    if num < 10000000 and li[num] != 0:
        return li[num]
    if num % 2 == 0:
        t = calculate(int(num / 2)) + 1
    else:
        t = calculate(num * 3 + 1) + 1
    if num < 10000000:
        li[num] = t
    return t


def main():
    num = 0
    mmax = 0
    for i in range(1, 1000000):
        t = calculate(i)
        if t > mmax:
            mmax = t
            num = i
    print("{}:{}".format(num, mmax))


if __name__ == '__main__':
    main()
