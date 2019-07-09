#include <iostream>
using namespace std;

int getSumOfDigits(int n) {
    int sum = 0;
    while (n > 0) { // 0 -> false, others -> true
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main() {
    // cout << getSumOfDigits(10) << endl;
    int N, A, B; cin >> N >> A >> B;
    int sum = 0;
    for (int i = 1; i <= N; ++i) {
        int sumDig = getSumOfDigits(i);
        // cout << "i: " << i << endl;
        // cout << "sumDig: " << sumDig << endl;
        if (sumDig >= A && sumDig <= B) {
            sum += i;
        }
    }
    cout << sum << endl;
}
