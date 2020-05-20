#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int,int>;

int main() {
    int N, M;
    vector<int> A(M), B(M);

    cin >> N >> M;
    rep(i, M) {
        int a, b;
        cin >> a >> b;
        A[i], B[i] = a - 1, b - 1;
    }

    

    return 0;
}