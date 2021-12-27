#include <iostream>

using namespace std;
//假如一个数前后掉转后还是同一个数的话，那个数就叫做「回文数」。由两个二位数的积构成的最大回文数是9009 = 91 × 99。
//请找出由两个三位数的积构成的最大回文数。

int is_palindromic_number(int number)
{
    int x = number;
    int temp = 0;
    while (x)
    {
        temp = temp * 10 + x % 10;
        x /= 10;
    }

    return temp == number;
}

int main()
{
    int ans = 0;
    for (int i = 999; i >= 100; i--)
    {
        for (int j = 999; j >= 100; j--)
        {
            int res = i * j;
            if (is_palindromic_number(res))
            {
                ans = max(ans, res);
            }
        }
    }
    cout << ans << endl;
}