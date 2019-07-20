#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>

using namespace std;

int main() {
    /*
        int の最大値は 4 bites 、すなわち 2^31 - 1 = 2147483647 である。
        よって、power が一時的にこれを越えてしまう場合があるから、long 型を用いる.`
     */

    int N;
    cin >> N;

    long long power = 1;
    for (int i = 1; i < N + 1; ++i)
    {
        power *= i;
        power %= int(pow(10, 9) + 7);
    }
    cout << power << endl;
}