#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> h(n);
    rep(i, n) {
        cin >> h[i];
    }

    if (n == 1) {
        cout << "Yes" << endl;
        return 0;
    }
    int max = 0;
    rep(i, n)
    {
        if (max - h[i] > 1) {
            cout << "No" << endl;
            return 0;
        }
        if (h[i] > max) max = h[i];
    }
    cout << "Yes" << endl;
}