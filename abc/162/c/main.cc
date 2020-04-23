#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int gcd(int a, int b) {
    if(b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

int main() {
    int K;
    cin >> K;

    int ans = 0;
    // int a = 0;
    for(int i = 1; i <= K; ++i) {
        for(int j = i; j <= K; ++j) {
            int tmp = gcd(i, j);
            for(int k = j; k <= K; ++k) {
                int a = gcd(tmp, k);
                if(i == j == k) {
                    ans += a;
                } else if(i == j || j == k) {
                    ans += a * 3;
                } else {
                    ans += a * 6;
                }
            }
        }
    }

    // for(int i = 1; i <= K; ++i) {
    //     for(int j = 1; j <= K; ++j) {
    //         int tmp = gcd(i, j);
    //         for(int k = 1; k <= K; ++k) {
    //             ans += gcd(tmp, k);
    //         }
    //     }
    // }
    cout << ans << endl;
    return 0;
}