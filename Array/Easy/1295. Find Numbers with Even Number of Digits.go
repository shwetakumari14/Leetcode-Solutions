package main

import (
	"fmt"
	"strconv"
)

func main() {

	nums := []int{12, 345, 2, 6, 7896}
	result := findNumbers(nums)
	fmt.Println(result)
}

func findNumbers(nums []int) int {
	count := 0

	for i := 0; i < len(nums); i++ {
		count += getDigitCount(nums[i])
	}

	return count
}

func getDigitCount(n int) int {
	counter := 0
	for n > 0 {
		n /= 10
		counter++
	}

	if counter%2 == 0 {
		return 1
	}

	return 0
}

func findNumbers1(nums []int) int {
	count := 0

	for i := 0; i < len(nums); i++ {
		str := strconv.Itoa(nums[i])
		if len(str)%2 == 0 {
			count++
		}
	}

	return count
}
