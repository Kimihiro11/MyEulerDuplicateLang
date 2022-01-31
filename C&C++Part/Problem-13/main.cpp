#include <iostream>
#include <cstring>
using namespace std;
#define MAX_N 100
int ans[MAX_N + 5];

int main()
{
    char s[MAX_N + 5];
    char stemp[MAX_N + 5];
    FILE *fp = fopen("./data.txt", "r");
    while (fscanf(fp, "%s", s) != EOF)
    {
        int n[MAX_N + 5] = {0};
        n[0] = strlen(s);
        for (int i = 0, j = n[0]; i < n[0]; i++, j--)
        {
            n[j] = s[i] - '0';
        }

        for (int i = 1; i <= MAX_N + 5; i++)
        {
            ans[i] += n[i];
            if (ans[i] > 9)
            {
                ans[i + 1]++;
                ans[i] %= 10;
            }
            if (ans[i])
                ans[0] = i;
        }
    }
    for (int i = ans[0]; i > ans[0] - 10; i--)
        cout << ans[i];
    cout << endl;
    return 0;
}