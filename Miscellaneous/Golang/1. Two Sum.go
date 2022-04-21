package main

import "fmt"

func main() {

	nums := []int{2, 7, 11, 15}
	target := 9

	result := twoSum(nums, target)
	fmt.Println(result)
}

func twoSum(nums []int, target int) []int {
	var ans []int
	tempMap := make(map[int]int)

	for i := 0; i < len(nums); i++ {
		_, ok := tempMap[target-nums[i]]
		if ok {
			ans = append(ans, tempMap[target-nums[i]])
			ans = append(ans, i)
			break
		}
		tempMap[nums[i]] = i
	}

	return ans
}
