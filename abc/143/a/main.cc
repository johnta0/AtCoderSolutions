#include <bits/stdc++.h>
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  int ans = a - 2 * b;
  if (ans < 0)
    ans = 0;
  cout << ans << endl;
}