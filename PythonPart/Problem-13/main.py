# -*- coding: utf-8 -*-
# @Time : 2022/1/31 下午1:29 
# @Author : kimihiro
# @File : main.py 
# @Software: PyCharm


# 大和
# 求以下一百个位数(data.txt)之和的前十位数字。

def main():
    with open("./data.txt", "r") as f:
        res = [int(i.replace("\n", "")) for i in f.readlines()]
    print((str((sum(res))))[:10])


if __name__ == '__main__':
    main()
