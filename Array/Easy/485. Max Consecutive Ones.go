package main

import "fmt"

func main() {

	arr := []int{1, 1, 0, 1, 1, 1}
	result := findMaxConsecutiveOnes(arr)
	fmt.Println(result)
}

func findMaxConsecutiveOnes(nums []int) int {
	count, result := 0, 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 1 {
			count++
			result = max(result, count)
		} else {
			count = 0
		}
	}

	return result
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
