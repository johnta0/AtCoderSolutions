#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int,int>;

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> X(M);
    rep(i, M) { cin >> X[i]; }

    if (N >= M) {
        cout << 0 << endl;
        return 0;
    }

    // 以下, N < M
    sort(X.begin(), X.end());
    vector<int> d(M - 1);
    rep(i, M - 1) { d[i] = X[i + 1] - X[i]; }

    sort(d.begin(), d.end());
    int ans = 0;
    rep(i, M - 1 - (N - 1)) { ans += d[i]; }
    cout << ans << endl;

    return 0;
}