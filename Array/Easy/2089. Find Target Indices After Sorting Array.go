package main

import (
	"fmt"
	"sort"
)

func main() {

	arr, target := []int{1, 2, 5, 2, 3}, 3
	result := targetIndices2(arr, target)
	fmt.Println(result)
}

func targetIndices(nums []int, target int) []int {

	sort.Ints(nums)
	var ans []int

	for i := 0; i < len(nums); i++ {
		if nums[i] == target {
			ans = append(ans, i)
		}
	}

	return ans
}

func targetIndices2(nums []int, target int) []int {

	var ans []int
	start, count := 0, 0

	for _, val := range nums {
		if val < target {
			start++
		} else if val == target {
			count++
		}
	}

	for i := 0; i < count; i++ {
		ans = append(ans, start+i)
	}

	return ans
}
