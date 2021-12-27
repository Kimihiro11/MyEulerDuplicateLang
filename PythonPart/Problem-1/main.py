# 如果列出小于10的所有是3或5的倍数的自然数，有3丶5丶6和9，它们的和是23。
# 现在请你算出所有1000以下为3或5的倍数的自然数的和。

def main():
    final_list = []
    for i in range(1000):
        if i % 3 == 0  or i % 5 == 0:
            final_list.append(i)
    final = sum(final_list)
    print(final)
if __name__ == "__main__":
    main()