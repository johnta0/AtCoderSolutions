#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> a(N);

    rep(i, N) cin >> a[i];
    vector<int> s = a;
    sort(s.rbegin(), s.rend());

    rep(i, N) {
        int ans = s[0];
        if (s[0] == a[i])
            ans = s[1];
        cout << ans << endl;
    }
}