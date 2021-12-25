package main

import "fmt"

func main() {

	arr := []int{0, 2, 1, 5, 3, 4}
	result := buildArrayPermutation(arr)
	fmt.Println(result)
}

func buildArrayPermutation(arr []int) []int {
	ans := make([]int, len(arr))
	for key := range arr {
		ans[key] = arr[arr[key]]
	}
	return ans
}
