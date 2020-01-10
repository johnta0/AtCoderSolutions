#include <math.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using namespace std;

int main() {
  int n;
  cin >> n;

  string ans = "No";

  rep(i, 1, 10) {
    if (n == i) {
      ans = "Yes";
      break;
    }
    if (i != 1 && n % i == 0 && n / i < 10) {
      ans = "Yes";
      break;
    }
  }
  cout << ans << endl;
}