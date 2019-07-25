#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>

#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;

/*
    https://atcoder.jp/contests/abc046/submissions/6538218
 */

int main() {
    int n, k;
    cin >> n >> k;

    int ans = k;
    if (k > 1) ans = ans * int(pow(k - 1, n - 1));
    cout << ans << endl;
    return 0;
}