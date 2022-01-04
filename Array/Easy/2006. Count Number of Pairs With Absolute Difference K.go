package main

import (
	"fmt"
	"math"
)

func main() {

	arr, k := []int{1, 2, 2, 1}, 1
	result := countKDifference2(arr, k)
	fmt.Println(result)
}

func countKDifference(nums []int, k int) int {

	count := 0

	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if int(math.Abs(float64(nums[i]-nums[j]))) == k {
				count++
			}
		}
	}

	return count
}

func countKDifference2(nums []int, k int) int {

	count := 0
	ansMap := make(map[int]int)

	for _, num := range nums {
		if val, ok := ansMap[num+k]; ok {
			count += val
		}
		if val, ok := ansMap[num-k]; ok {
			count += val
		}

		ansMap[num]++
	}

	return count
}
