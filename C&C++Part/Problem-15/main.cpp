#include <iostream>

using namespace std;

long long li[25][25];

int main()
{
    for (int i = 1; i < 22; i++)
    {
        for (int j = 1; j < 22; j++)
        {
            if (i == 1 && j == 1)
            {
                li[i][j] = 1;
                continue;
            }
            li[i][j] = li[i - 1][j] + li[i][j - 1];
        }
    }
    cout << li[21][21] << endl;
    return 0;
}