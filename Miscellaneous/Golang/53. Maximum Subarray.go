package main

import (
	"fmt"
	"math"
)

func main() {

	arr := []int{5, 4, -1, 7, 8}
	result := maxSubArrsum(arr)
	fmt.Println(result)
}

func maxSubArrsum(arr []int) int {
	maxSoFar, maxEndingHere := math.MinInt, 0

	for i := 0; i < len(arr); i++ {
		maxEndingHere += arr[i]

		if maxSoFar < maxEndingHere {
			maxSoFar = maxEndingHere
		}

		if maxEndingHere < 0 {
			maxEndingHere = 0
		}
	}

	return maxSoFar
}
