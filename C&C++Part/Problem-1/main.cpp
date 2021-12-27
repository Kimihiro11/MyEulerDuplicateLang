#include <iostream>
using namespace std;

//如果列出小于10的所有是3或5的倍数的自然数，有3丶5丶6和9，它们的和是23。
//现在请你算出所有1000以下为3或5的倍数的自然数的和。
int main() {
    int ans = 0;
    for (int i = 1; i < 1000; i++){
        if (i % 3== 0 || i % 5==0)
        {
            ans += i;
        }
    }
    cout << ans << endl;
    return 0;
}