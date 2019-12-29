#include <bits/stdc++.h>
#define rep(i, s, n) for (int i = s; i < (int)(n); ++i)
using namespace std;

int main() {
    int N;

    cin >> N;
    vector<int> d(N);
    rep(i, 0, N) {
        cin >> d.at(i);
    }

    int sum = 0;
    rep(i, 0, N - 1) {
        rep(j, i + 1, N) {
            sum += d[i] * d[j];
        }
    }
    cout << sum << endl;
}