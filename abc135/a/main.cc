#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    int c = a + b;
    if (c % 2 == 1)
        cout << "IMPOSSIBLE" << endl;
    else
        cout << c / 2 << endl;
}