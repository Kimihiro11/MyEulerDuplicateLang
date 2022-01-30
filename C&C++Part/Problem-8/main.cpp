#include <iostream>
using namespace std;
// 你能够从以下的1000位的数字中，连续十三个数字的最大乘积，其积最大吗？

char str[1024];
int main()
{
    long long res = 0, now = 1;
    int zero = 0;

    cin >> str;
    for (int i = 0; str[i]; i++)
    {
        if (i < 13)
        {
            now *= str[i] - '0';
        }
        else if (str[i] != '0')
        {
            now *= str[i] - '0';
        }
        else
        {
            zero++;
        }
        if (i >= 13)
        {
            if (str[i - 13] != '0')
            {
                now /= str[i - 13] - '0';
            }
            else
            {
                zero--;
            }
        }
        if (zero == 0)
        {
            res = max(res, now);
        }
    }
    cout << res << endl;
    return 0;
}