#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    int k, a, b;
    cin >> k >> a >> b;

    int now = k;
    while(now <= 1000) {
        if(now >= a && now <= b) {
            // cout << now << endl;
            cout << "OK" << endl;
            return 0;
        }
        now += k;
    }
    cout << "NG" << endl;
    return 0;
}