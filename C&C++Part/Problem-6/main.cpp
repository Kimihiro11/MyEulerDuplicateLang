#include <iostream>
using namespace std;
//  前十个正整数的平方和是：12 + 22 + ... + 102 = 385
//  前十个正整数的和的平方是：(1 + 2 + ... + 10)2 = 552 = 3025
//  因此前十个正整数的和的平方，与前十个正数整数的平方和，的差是2640。
//  现在请你求出前一百个正整数的和的平方与前一百个正整数的平方和的差。
int main()
{
    int sum = 0, psum = 0;
    for (int i = 1; i <= 100; i++)
    {
        sum += i;
        psum += i * i;
    }
    cout << sum * sum - psum << endl;
}