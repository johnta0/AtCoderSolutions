#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

void yes()
{
    cout << "YES" << endl;
}

/*
    https://atcoder.jp/contests/abs/tasks/arc065_a
    1 <= |S| <= 10^5
 */

int main()
{
    string S;
    cin >> S;
    vector<string> words = {"dream", "dreamer", "erase", "eraser"};

    int len = S.length();
    string comb = "";

    if (len < 5)
        break;
    if (len == 5 && (S == words[0] || S == words[2]))
    {
        yes();
        return 0;
    }
    if (len == 6 && S == words[3])
    {
        yes();
        return 0;
    }
    if (len == 7 && S == words[1])
    {
        yes();
        return 0;
    }

    int pos = 4;
    while (pos < len)
    {
        
    }

        cout << "NO" << endl;
}