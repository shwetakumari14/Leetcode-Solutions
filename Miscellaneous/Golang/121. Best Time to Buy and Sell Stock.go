package main

import "fmt"

func main() {

	arr := []int{7, 1, 5, 3, 6, 4}
	result := maxProfit(arr)
	fmt.Println(result)
}

func maxProfit(arr []int) int {
	maxDiff, idx := 0, arr[0]

	for i := 1; i < len(arr); i++ {
		profit := arr[i] - idx
		maxDiff = max(maxDiff, profit)
		if idx > arr[i] {
			idx = arr[i]
		}
	}

	return maxDiff
}

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}
