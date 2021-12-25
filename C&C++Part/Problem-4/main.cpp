#include <iostream>

using namespace std;

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