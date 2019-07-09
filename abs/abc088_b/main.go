package main

import (
	"fmt"
	"sort"
)

func main() {
	var (
		N     int
		alice int
		bob   int
	)
	fmt.Scan(&N)

	a := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&a[i])
	}

	sort.Sort(sort.Reverse(sort.IntSlice(a)))

	for i := 0; i < N; i++ {
		if i%2 == 0 {
			alice += a[i]
		} else {
			bob += a[i]
		}
	}
	fmt.Println(alice - bob)
}
