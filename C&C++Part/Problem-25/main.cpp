#include <iostream>
using namespace std;

int a = 0, b = 1, num[2][1005] = {{1, 1}, {1, 1}};

int func(int x, int y)
{
    num[y][0] = num[x][0];
    for (int i = 1; i <= num[y][0]; i++)
    {
        num[y][i] += num[x][i];
        if (num[y][i] > 9)
        {
            num[y][i + 1] += num[y][i] / 10;
            num[y][i] %= 10;
            if (num[y][0] == i)
                num[y][0]++;
        }
    }
    return num[y][0] == 1000;
}

int main()
{
    cout << (sizeof(num[0]) / sizeof(int)) << endl;

    for (int i = 3; 1; i++)
    {
        if (func(b, a))
        {
            cout << i << endl;
            break;
        }
        swap(a, b);
    }
    return 0;
}