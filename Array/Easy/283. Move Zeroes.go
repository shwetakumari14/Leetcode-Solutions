package main

import "fmt"

func main() {

	arr := []int{0, 1, 0, 3, 12}
	moveZeroes(arr)
	fmt.Println(arr)
}

func moveZeroes(nums []int) {
	var ans []int
	count := 0

	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			count++
		} else {
			ans = append(ans, nums[i])
		}
	}

	for count > 0 {
		ans = append(ans, 0)
		count--
	}

	copy(nums, ans)
}

func moveZeroes2(nums []int) {
	idx := 0

	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[idx] = nums[i]
			idx++
		}
	}

	for idx < len(nums) {
		nums[idx] = 0
		idx++
	}

}
