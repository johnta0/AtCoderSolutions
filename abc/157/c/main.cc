#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int N, M;
int ss[5], cc[5];

int main() {
  cin >> N >> M;
  rep(i, M) cin >> ss[i] >> cc[i];

  int ans = -1;
  if (M == 0) {
    if (N == 1) {
      ans = 0
      cout << ans << endl;
      return 0;
    } else {
      ans = pow(10, N -1)
      cout << ans << endl;
      return 0;
    }
  }

  for (int i = int(pow(10, N - 1)) - 1; i < int(pow(10, N)) - 1; ++i) {
    if (N != 1 && i == int(pow(10, N - 1)) - 1) continue;
    string i_str = to_string(i);
    rep(m, M) {
      if (i_str.at(ss[m] - 1) != to_string(cc[m])) break;
      if (m == M - 1) {
        ans = i;
        cout << ans << endl;
      }
    }
  }

  cout << ans << endl;
  return 0;
}