#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

// void printVec(vector<int> &vec) {
//     cout << "";
//     for (auto it = vec.begin(); it != vec.end(); ++it)
//         cout << *it << " ";
//     cout << endl;
// }

int main() {
    int N;
    cin >> N;
    vector<int> d(N);
    for(int i = 0; i < N; ++i)
        cin >> d.at(i);

    // 同じ大きさの鏡餅は複数あっても意味がない => 重複は除く
    sort(d.begin(), d.end());
    d.erase(unique(d.begin(), d.end()), d.end());

    // 重複排除後の長さを表示
    cout << d.size() << endl;
    return 0;
}
