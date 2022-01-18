package main

import "fmt"

func main() {

	nums := []int{4, 2, 5, 7}
	result := sortArrayByParityII(nums)
	fmt.Println(result)
}

func sortArrayByParityII(nums []int) []int {
	result := make([]int, len(nums))

	for i, j, k := 0, 0, 1; i < len(nums); i++ {
		if nums[i]%2 == 0 {
			result[j] = nums[i]
			j += 2
		} else {
			result[k] = nums[i]
			k += 2
		}
	}

	return result
}

func sortArrayByParityII2(nums []int) []int {

	i, j := 0, len(nums)-1

	for i < len(nums) && j >= 1 {
		if nums[i]%2 == 0 {
			i += 2
		} else if nums[j]%2 == 1 {
			j -= 2
		} else {
			nums[i], nums[j] = nums[j], nums[i]
		}
	}

	return nums
}
