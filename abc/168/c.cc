#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;
#define PI 3.14159265358979323846264338327950L

int main() {
    int a, b, h, m;
    cin >> a >> b >> h >> m;

    long double ang_h = (long double)( h / 12.0 ) * 2 * PI;
    long double ang_m = (long double) (m / 60) * 2 * PI;
    long double ang_diff = abs(ang_h - ang_m);

    if(ang_diff > PI) {
        ang_diff = 2 * PI - ang_diff;
    }

    long double ans = sqrtl( (long double)(a * a + b * b) - (long double )(2 * a * b) * cosl(ang_diff));

    cout << ans << endl;
    return 0;
}