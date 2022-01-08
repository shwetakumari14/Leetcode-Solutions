package main

import "fmt"

func main() {
	arr := []int{2, 5, 6, 9, 10}
	result := findGCD(arr)
	fmt.Println(result)
}

func findGCD(nums []int) int {
	min, max := nums[0], nums[0]

	for i := 1; i < len(nums); i++ {
		if nums[i] > max {
			max = nums[i]
		}
		if nums[i] < min {
			min = nums[i]
		}
	}

	for max != min {
		if max > min {
			max -= min
		} else {
			min -= max
		}
	}

	return max
}
