package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main()  {
	var (
		n int
	)
	fmt.Scan(&n)
	
	a := make([][]int, n)
	reader := NewReader()
	for i := range a {
		a[i] = reader.ReadInts()
	}

	dp := make([][]int, n + 1)
	for i := range dp {
		dp[i] = make([]int, 3)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < 3; j++ {
			for k := 0; k < 3; k++ {
				if j == k { continue }
				dp[i + 1][k] = Max(dp[i + 1][k], dp[i][j] + a[i][k])	
			}
		}
	}
	ans := 0
	for i := 0; i < 3; i++ {
		ans = Max(ans, dp[n][i])
	}
	fmt.Println(ans)
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
 
func MaxInts(n ...int) int {
	max := n[0]
	for _, v := range n[1:] {
		if v > max {
			max = v
		}
	}
	return max
}
 
type Reader struct {
	r    *bufio.Reader
	size int
	sep  string
}
 
func NewReader() *Reader {
	size := 4096
	return &Reader{
		r:    bufio.NewReaderSize(os.Stdin, size),
		size: size,
		sep:  " ",
	}
}
 
func (rdr *Reader) ReadLine() string {
	buf := make([]byte, 0, rdr.size)
	for {
		line, isPrefix, err := rdr.r.ReadLine()
		if err != nil {
			panic(err)
		}
		buf = append(buf, line...)
		if !isPrefix {
			break
		}
	}
	return string(buf)
}
 
func (rdr *Reader) ReadStrs() []string {
	return strings.Split(rdr.ReadLine(), rdr.sep)
}
 
func (rdr *Reader) ReadInts() []int {
	a := rdr.ReadStrs()
	b := make([]int, len(a))
	for i, v := range a {
		b[i], _ = strconv.Atoi(v)
	}
	return b
}
