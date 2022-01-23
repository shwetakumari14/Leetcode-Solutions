package main

import "fmt"

func main() {

	arr := []int{1, 7, 3, 6, 5, 6}
	result := pivotIndex(arr)
	fmt.Println(result)
}

func pivotIndex(nums []int) int {
	rightSum, leftSum := 0, 0

	for _, val := range nums {
		rightSum += val
	}

	for i := 0; i < len(nums); i++ {
		rightSum -= nums[i]
		if leftSum == rightSum {
			return i
		}
		leftSum += nums[i]

	}

	return -1
}
