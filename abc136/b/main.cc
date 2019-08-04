#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;

int main()
{
    int n;
    cin >> n;

    int d = 0;
    rep(i, 7)
    {
        if (n < pow(10, i))
        {
            d = i;
            break;
        }
    }

    int c = 0;
    for (int i = 1; i < d + 1; ++i)
    {
        if (i % 2 == 0)
            continue;
        if (i == d)
        {
            c += n - pow(10, i - 1) + 1;
            break;
        }
        c += pow(10, i) - pow(10, i - 1);
    }
    cout << c << endl;
}