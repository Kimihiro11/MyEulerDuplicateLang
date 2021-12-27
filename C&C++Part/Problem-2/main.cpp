#include <iostream>

using namespace std;
//Fibonacci数列的每后一项都是前面两项的和，若开始的头两项是1和2，那么前10个项就是：
//1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
//请求出以上Fibonacci数列中不超过400,0000的所有偶数的和。
int main()
{
    long long ans = 0;
    int a = 1;
    int b = 2;
    while (b < 4000000)
    {
        if (b % 2 == 0)
        {
            ans += b;
        }
        b = a + b;
        a = b - a;
    }
    cout << ans << endl;
}
