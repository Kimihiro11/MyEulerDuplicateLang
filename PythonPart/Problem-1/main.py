def main():
    final_list = []
    for i in range(1000):
        if i % 3 == 0  or i % 5 == 0:
            final_list.append(i)
    final = sum(final_list)
    print(final)
if __name__ == "__main__":
    main()