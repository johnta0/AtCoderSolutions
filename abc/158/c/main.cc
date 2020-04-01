#include <bits/stdc++.h>
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
  int a, b;
  cin >> a >> b;

  int ans = 0;
  rep(i, 0, 1300) {
    int za = i * 0.08;
    int zb = i * 0.10;
    if (a == za && b == zb) {
      cout << i << endl;
      return 0;
    }
  }
  cout << -1 << endl;
  return 0;
}