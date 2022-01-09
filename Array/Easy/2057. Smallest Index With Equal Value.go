package main

import "fmt"

func main() {

	arr := []int{4, 3, 2, 1}
	result := smallestEqual(arr)
	fmt.Println(result)
}

func smallestEqual(nums []int) int {

	for i := 0; i < len(nums); i++ {
		if i%10 == nums[i] {
			return i
		}
	}

	return -1
}
