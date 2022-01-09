package main

import "fmt"

func main() {

	arr := []int{3, 1, 2, 4}
	result := sortArrayByParity1(arr)
	fmt.Println(result)
}

func sortArrayByParity(nums []int) []int {

	var ans []int

	for _, val := range nums {
		if val%2 == 0 {
			ans = append(ans, val)
		}
	}

	for _, val := range nums {
		if val%2 == 1 {
			ans = append(ans, val)
		}
	}

	return ans
}

func sortArrayByParity1(nums []int) []int {

	pointer := 0

	for i := 0; i < len(nums); i++ {
		if nums[i]%2 == 0 {
			nums[pointer], nums[i] = nums[i], nums[pointer]
			pointer++
		}
	}

	return nums
}
