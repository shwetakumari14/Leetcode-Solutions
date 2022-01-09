package main

import "fmt"

func main() {

	arr := []int{5, 1, 5, 2, 5, 3, 5, 4}
	result := repeatedNTimes(arr)
	fmt.Println(result)

}

func repeatedNTimes(nums []int) int {

	ansMap := make(map[int]int)

	for i := 0; i < len(nums); i++ {
		_, ok := ansMap[nums[i]]
		if ok {
			return nums[i]
		}
		ansMap[nums[i]]++
	}

	return -1
}
