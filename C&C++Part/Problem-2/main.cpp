#include <iostream>

using namespace std;

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
