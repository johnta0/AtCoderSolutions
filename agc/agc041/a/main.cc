#include <bits/stdc++.h>
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using namespace std;

int main() {
  long long n, a, b, d;
  cin >> n >> a >> b;
  d = (b - a) / 2;

  if ((b - a) % 2 == 0) {
    cout << d << endl;
  } else {
    if (n - a > b - 1) {
      cout << b - 1 << endl;
    } else {
      cout << n - a << endl;
    }
  }

  return 0;
}
