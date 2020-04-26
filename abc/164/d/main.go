package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s string
	fmt.Scan(&s)
	// fmt.Println(s)
	N := len(s)

	cnt := 0
	for i := 0; i <= N - 4; i++ {
		for j := i + 4; j <= N; j++ {
			num, _ := strconv.Atoi(s[i : j])
			if num % 2019 == 0 {
				cnt++
			}
		}
	}
	fmt.Println(cnt)
}
