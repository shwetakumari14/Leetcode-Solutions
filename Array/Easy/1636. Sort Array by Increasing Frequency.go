package main

import (
	"fmt"
	"sort"
)

func main() {

	arr := []int{1, 1, 2, 2, 2, 3}
	result := frequencySort(arr)
	fmt.Println(result)
}

func frequencySort(nums []int) []int {

	numsMap := make(map[int]int)

	for _, val := range nums {
		numsMap[val]++
	}

	sort.Slice(nums, func(i, j int) bool {
		if numsMap[nums[i]] == numsMap[nums[j]] {
			return nums[j] < nums[i]
		}

		return numsMap[nums[i]] < numsMap[nums[j]]
	})

	return nums
}
