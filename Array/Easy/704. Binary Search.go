package main

import "fmt"

func main() {

	arr, target := []int{5}, 5
	result := search(arr, target)
	fmt.Println(result)
}

func search(nums []int, target int) int {
	mid, low, hi := 0, 0, len(nums)-1

	for low <= hi {
		mid = (low + hi) / 2
		if target > nums[mid] {
			low += 1
		} else if target < nums[mid] {
			hi -= 1
		} else {
			return mid
		}
	}

	return -1
}
