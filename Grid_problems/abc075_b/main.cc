#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    int H, W;
    cin >> H >> W;
    // vector<vector<char> S(H, vector<char>(W, 0));
    for (int i = 0; i < H; ++i){
        char* s;
        cin >> s;
        for (int j = 0; j < W; ++j) {
            S[i][j] = s[j];
        }
    }
    
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            cout << S[i][j] << " ";
        }
        cout << endl;
    }
}