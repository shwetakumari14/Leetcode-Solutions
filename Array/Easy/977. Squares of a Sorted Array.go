package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {

	arr := []int{-4, -1, 0, 3, 10}
	result := sortedSquares1(arr)
	fmt.Println(result)
}

func sortedSquares(nums []int) []int {

	for key, val := range nums {
		nums[key] = val * val
	}
	sort.Ints(nums)

	return nums
}

func sortedSquares1(nums []int) []int {

	ans := make([]int, len(nums))
	start, end, pos := 0, len(nums)-1, len(nums)-1

	for start <= end {
		if math.Abs(float64(nums[start])) > math.Abs(float64(nums[end])) {
			ans[pos] = nums[start] * nums[start]
			start++
			pos--
		} else {
			ans[pos] = nums[end] * nums[end]
			end--
			pos--
		}
	}

	return ans
}
