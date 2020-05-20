#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int,int>;

int main() {
    int A, B, C, X;
    cin >> A >> B >> C >> X;

    int cnt = 0;
    rep(a, A + 1) {
        rep(b, B + 1) {
            rep(c, C + 1) {
                if (500 * a + 100 * b + 50 * c == X) {
                    cnt++;
                }
            }
        }
    }
    cout << cnt << endl;
    return 0;
}