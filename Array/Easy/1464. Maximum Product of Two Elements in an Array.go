package main

import (
	"fmt"
	"sort"
)

func main() {

	arr := []int{3, 4, 5, 2}
	result := maxProduct2(arr)
	fmt.Println(result)
}

func maxProduct(nums []int) int {
	sort.Ints(nums)
	n := len(nums)
	return (nums[n-2] - 1) * (nums[n-1] - 1)
}

func maxProduct2(nums []int) int {
	max1, max2 := nums[0], 0

	for i := 1; i < len(nums); i++ {
		if max1 < nums[i] {
			max2 = max1
			max1 = nums[i]
		} else if max2 < nums[i] {
			max2 = nums[i]
		}
	}

	return (max1 - 1) * (max2 - 1)
}
