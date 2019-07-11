#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void printNums(int a, int b, int c)
{
    cout << a << " ";
    cout << b << " ";
    cout << c << endl;
}

int main()
{

    /*
        日本でよく使われる紙幣は、 10000円札、5000円札、1000円札です。
        以下、「お札」とはこれらのみを指します。

        青橋くんが言うには、彼が祖父から受け取ったお年玉袋にはお札が N枚入っていて、合計で 
        Y円だったそうですが、嘘かもしれません。このような状況がありうるか判定し、
        ありうる場合はお年玉袋の中身の候補を一つ見つけてください。なお、彼の祖父は十分裕福であり、
        お年玉袋は十分大きかったものとします。
     */

    int N, Y;
    cin >> N >> Y;

    // 以下の場合分けは、速度が向上しないので不必要。

    // if (N * 1000 == Y) {
    //     printNums(0, 0, N);
    //     return 0;
    // }
    // if (N * 5000 == Y) {
    //     printNums(0, N, 0);
    //     return 0;
    // }
    // if (N * 10000 == Y) {
    //     printNums(N, 0, 0);
    //     return 0;
    // }

    // if (N* 1000 > Y && (N-1) * 1000 + 10000 < Y) {
    //     printNums(-1, -1, -1);
    //     return 0;
    // }
    // if (N * 5000 > Y && (N-1) * 5000 + 10000 < Y) {
    //     printNums(-1, -1, -1);
    //     return 0;
    // }
    // if (N * 10000 > Y && (N-1) * 10000 + 5000 < Y) {
    //     printNums(-1, -1, -1);
    //     return 0;
    // }

    for (int i = 0; i <= N; ++i)
    {
        for (int j = 0; j <= N - i; ++j)
        {
            int k = N - i - j;
            printNums(i, j, k);
            return 0;
        }
    }
}
}
printNums(-1, -1, -1);
}