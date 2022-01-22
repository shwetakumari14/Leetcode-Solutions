package main

import "fmt"

func main() {

	n := 5
	result := arrangeCoins(n)
	fmt.Println(result)
}

func arrangeCoins(n int) int {
	counter, level := 1, 0

	for n > 0 {
		n -= counter
		counter++
		if n >= 0 {
			level++
		}
	}

	return level
}
