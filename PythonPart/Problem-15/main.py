# -*- coding: utf-8 -*-
# @Time : 2022/2/4 下午1:35 
# @Author : kimihiro
# @File : main.py
# @Software: PyCharm


# 从一个2×2的方格的左上角开始，共有6条路径可达到右下角（不能后退）
# 请问，假如把上述方格的规模改成20×20，共有多少条路径呢？
from pprint import pprint


def main():
    ori = [0 for i in range(25)]
    li = [ori for i in range(25)]
    for i in range(1, 22):
        for j in range(1, 22):
            if i == 1 and j == 1:
                li[i][j] = 1
                continue
            li[i][j] = li[i - 1][j] + li[i][j - 1]
    print(li[21][21])


if __name__ == '__main__':
    main()
