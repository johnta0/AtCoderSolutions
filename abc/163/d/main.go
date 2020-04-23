package main

import (
	"fmt"
	"bufio"
	"os"
)

var (
	N, K int
	M, m int
)

func main () {
	r := bufio.NewReader(os.Stdin)
	fmt.Fscan(r, &N)
	fmt.Fscan(r, &K)

	mod := 1000000007
	ans := 0
	for k := K; k <= N + 1; k++ {
		M = sumOfNums(N - k + 1, N)
		m = sumOfNums(0, k - 1)
		ans += M - m + 1
		ans %= mod
	}
	fmt.Println(ans)
}

func sumOfNums(l, r int) int {
	return (l + r) * (r - l + 1) / 2
}
