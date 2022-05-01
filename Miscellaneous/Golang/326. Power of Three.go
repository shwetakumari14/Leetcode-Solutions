package main

import "fmt"

func main() {

	n := 27
	result := isPowerOfThree(n)
	fmt.Println(result)
}

func isPowerOfThree(n int) bool {
	if n < 1 {
		return false
	} else if n == 1 {
		return true
	}

	val := 1

	for val < n {
		val *= 3
		if val == n {
			return true
		}
	}

	return false
}
