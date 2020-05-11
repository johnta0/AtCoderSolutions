#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int,int>;

int main() {
    ll X;
    cin >> X;

    ll bal = 100;
    ll ans = 1;
    while (bal < X) {
        bal += bal / 100;
        if(bal >= X) {
            cout << ans << endl;
        }
        ans++;
    }
    return 0;
}