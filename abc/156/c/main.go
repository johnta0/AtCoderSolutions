package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	// "strings"
	"math"
)

var (
	n int
	scanner = bufio.NewScanner(os.Stdin)
)

const (
	MAX = 1000000000000
)

func main() {
	scanner.Split(bufio.ScanWords)
	n := scanInt()
	xx := scanInts(n)

	ans := MAX
	for p := 1; p <= 100; p++ {
		hp := 0
		for _, x := range xx {
			hp += (x - p) * (x - p)
		}
		ans = Min(ans, hp)
	}
	fmt.Println(ans)
}

func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func scanInt() int {
	i, _ := strconv.Atoi(scanText())
	return i
}

func scanInts(size int) []int {
	ints := make([]int, size)
	for i := 0; i < size; i++ {
		ints[i] = scanInt()
	}
	return ints
}

func scanText() string {
	scanner.Scan()
	return scanner.Text()
}

func min(n []int) (min, idx int) {
	min = math.MaxInt64
	for i := 0; i < len(n); i++ {
		if n[i] < min {
			min = n[i]
			idx = i
		}
	}
	return
}

func max(n []int) (max, idx int) {
	max = math.MinInt64
	for i := 0; i < len(n); i++ {
		if n[i] > max {
			max = n[i]
			idx = i
		}
	}
	return
}

