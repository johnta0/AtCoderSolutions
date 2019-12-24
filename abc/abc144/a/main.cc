#include <math.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;

  if (a < 10 && b < 10) {
    cout << a * b << endl;
  } else {
    cout << -1 << endl;
  }
}