#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int N; cin >> N;
    int a[N] = {0};
    for (int i = 0; i < N; ++i) cin >> a[i];
    sort(a, a + N, greater<int>());

    int alice = 0, bob = 0;
    for (int i = 0; i < N; ++i) {
        if (i % 2 == 0)
            alice += a[i];
        else {
            bob += a[i];
        }
    }
    cout << alice - bob << endl;
}
