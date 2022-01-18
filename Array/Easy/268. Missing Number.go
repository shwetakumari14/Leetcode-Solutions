package main

import "fmt"

func main() {

	arr := []int{3, 0, 1}
	result := missingNumber(arr)
	fmt.Println(result)
}

func missingNumber(nums []int) int {
	n := len(nums)
	sum := (n) * (n + 1) / 2
	for _, val := range nums {
		sum -= val
	}
	return sum
}
