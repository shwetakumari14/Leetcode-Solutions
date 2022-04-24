package main

import "fmt"

func main() {

	x := 17
	result := sqrt(x)
	fmt.Println(result)
}

func sqrt(x int) int {
	if x == 0 {
		return 0
	}

	left, right := 1, x

	for left < right-1 {
		mid := left + (right-left)/2
		if mid <= x/mid {
			left = mid
		} else {
			right = mid - 1
		}
	}

	if right <= x/right {
		return right
	}

	return left
}
