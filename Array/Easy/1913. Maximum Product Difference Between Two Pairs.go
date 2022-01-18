package main

import (
	"fmt"
	"sort"
)

func main() {

	arr := []int{10, 10, 10, 10}
	result := maxProductDifference(arr)
	fmt.Println(result)
}

func maxProductDifference(nums []int) int {
	sort.Ints(nums)
	n := len(nums)

	return nums[n-1]*nums[n-2] - nums[0]*nums[1]
}
