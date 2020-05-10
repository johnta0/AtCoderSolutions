#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    int n, m, c;
    cin >> n >> m >> c;

    vector<int> B(m);
    int ans = 0;
    rep(i, m) { cin >> B.at(i); }
    rep(i, n) {
        int sum = 0;
        rep(i, m) {
            int tmp;
            cin >> tmp;
            sum += tmp * B[i];
        }
        if(sum + c > 0) {
            ans++;
        }
    }
    cout << ans << endl;
}
