package main

import (
	"fmt"
	"sort"
)

func main() {

	arr := []int{8, 1, 2, 2, 3}
	result := smallerNumbersThanCurrent1(arr)
	fmt.Println(result)
}

func smallerNumbersThanCurrent(nums []int) []int {

	var ans []int

	for i := 0; i < len(nums); i++ {
		count := 0
		for j := 0; j < len(nums); j++ {
			if nums[i] > nums[j] && i != j {
				count++
			}
		}
		ans = append(ans, count)
	}

	return ans

}

func smallerNumbersThanCurrent1(nums []int) []int {

	temp := make([]int, len(nums))
	copy(temp, nums)
	sort.Ints(temp)
	ansMap := make(map[int]int)

	for i := 0; i < len(temp); i++ {
		_, ok := ansMap[temp[i]]
		if !ok {
			ansMap[temp[i]] = i
		}
	}

	result := make([]int, len(nums))
	for i := 0; i < len(nums); i++ {
		result[i] = ansMap[nums[i]]
	}

	return result
}
