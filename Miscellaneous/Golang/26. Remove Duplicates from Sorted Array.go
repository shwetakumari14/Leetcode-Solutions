package main

import (
	"fmt"
)

func main() {

	nums := []int{1, 1, 2}
	result := removeDuplicates(nums)
	fmt.Println(result)
}

func removeDuplicates(arr []int) int {
	keys := make(map[int]bool)
	var ans []int
	for i := 0; i < len(arr); i++ {
		if _, ok := keys[arr[i]]; !ok {
			keys[arr[i]] = true
			ans = append(ans, arr[i])
		}
	}

	return len(ans)
}
