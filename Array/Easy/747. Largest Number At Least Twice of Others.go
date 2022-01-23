package main

import "fmt"

func main() {

	arr := []int{3, 6, 1, 0}
	result := dominantIndex(arr)
	fmt.Println(result)
}

func dominantIndex(nums []int) int {
	maxNum, maxIdx := 0, -1

	for i := 0; i < len(nums); i++ {
		if maxNum < nums[i] {
			maxNum = nums[i]
			maxIdx = i
		}
	}

	for i := 0; i < len(nums); i++ {
		if i != maxIdx && maxNum < nums[i]*2 {
			return -1
		}
	}

	return maxIdx
}
