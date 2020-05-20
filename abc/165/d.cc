#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    ll a, b, n;
    cin >> a >> b >> n;

    ll x = min(b - 1, n);
    int ans = int(a * x / b) - a * int(x / b);
    // // 全探索
    // ll ans = 0;
    // for(ll x = 0; x <= n; ++x) {
    //     ll fst = a * x / b;
    //     ll scd = x / b;
    //     scd *= a;
    //     ll flr = fst - scd;
    //     ans = max(ans, flr);
    // }
    cout << ans << endl;
    return 0;
}