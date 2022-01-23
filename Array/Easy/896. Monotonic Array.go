package main

import (
	"fmt"
)

func main() {

	nums := []int{1, 2, 2, 3}
	result := isMonotonic(nums)
	fmt.Println(result)
}

func isMonotonic(nums []int) bool {
	n := len(nums)
	for i := 1; i < len(nums); i++ {
		if nums[0] <= nums[n-1] {
			if nums[i-1] > nums[i] {
				return false
			}
		} else {
			if nums[i-1] < nums[i] {
				return false
			}
		}
	}

	return true
}
