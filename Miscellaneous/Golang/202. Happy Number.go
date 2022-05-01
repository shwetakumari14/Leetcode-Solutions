package main

import "fmt"

func main() {

	n := 19
	result := happyNumber(n)
	fmt.Println(result)
}

func happyNumber(n int) bool {
	tempMap := make(map[int]bool)
	tempMap[n] = true

	for {
		sum, x, r := 0, n, 0
		for x > 0 {
			r = x % 10
			sum += r * r
			x /= 10
		}
		exists := tempMap[sum]
		if exists {
			break
		}
		tempMap[n] = true
		n = sum
	}

	if n == 1 {
		return true
	}
	return false
}
