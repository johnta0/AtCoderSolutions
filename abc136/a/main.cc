#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    int d = 0;
    if (c - (a - b) > 0)
        d = c - (a - b);

    cout << d << endl;
}