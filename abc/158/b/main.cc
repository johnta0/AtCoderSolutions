#include <bits/stdc++.h>
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
  ll n, a, b;
  cin >> n >> a >> b;

  ll q = n / (a + b);
  n -= q * (a + b);

  ll ans = q * a + min(n, a);

  cout << ans << endl;
  return 0;
}
