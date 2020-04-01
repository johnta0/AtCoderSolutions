#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

// input
int N, W;
int weight[110];
ll value[110];
// dp table
ll dp[110][100010];

int main() {
  cin >> N >> W;
  rep(i, N) cin >> weight[i] >> value[i];

  // initialize
  rep(w, W + 1) dp[0][w] = 0;

  // dp
  rep(i, N) {
    rep(w, W + 1) {
      if (w < weight[i]) {
        dp[i + 1][w] = dp[i][w];
      } else {
        dp[i + 1][w] = max(dp[i][w], dp[i][w - weight[i]] + value[i]);
      }
    }
  }
  cout << dp[N][W] << endl;

  return 0;
}
