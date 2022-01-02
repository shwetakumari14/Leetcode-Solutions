package main

import "fmt"

func main() {

	nums := []int{0, 1, 2, 3, 4}
	index := []int{0, 1, 2, 2, 1}
	result := createTargetArray(nums, index)
	fmt.Println(result)
}

func createTargetArray(nums []int, index []int) []int {

	target := make([]int, len(nums))
	checkStatus := make([]bool, len(nums))

	for i := 0; i < len(nums); i++ {
		if checkStatus[index[i]] == false && target[index[i]] == 0 {
			target[index[i]] = nums[i]
			checkStatus[index[i]] = true
		} else {
			rightShiftArray(target, index[i])
			target[index[i]] = nums[i]
		}

	}
	return target
}

func rightShiftArray(nums []int, i int) {
	tmp, tmp1 := nums[i], 0
	for j := i + 1; j < len(nums); j++ {
		tmp1 = nums[j]
		nums[j] = tmp
		tmp = tmp1
	}
}
