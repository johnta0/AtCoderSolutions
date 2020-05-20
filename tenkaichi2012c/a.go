package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
	"strings"
	"math"
)

func isPrime(num int) bool {
	if num == 1 { return false}
	for k := 2; k <= int(math.Sqrt(float64(num))); k++ {
		if num % k == 0 { return false }
	}
	return true
}

func main() {
	n, _ := readInt() // 1 <= n <= 10,000
	primeCount := 0
	for i := 2; i < n; i++ {
		if isPrime(i) { primeCount++ }
	}
	fmt.Println(primeCount)
}



func readStr() (ret string) {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	inpStr := scanner.Text()
	ret = strings.TrimSpace(inpStr)
	return
}

func readInt() (int, error) {
	inpStr := readStr()
	return strconv.Atoi(inpStr)
}
