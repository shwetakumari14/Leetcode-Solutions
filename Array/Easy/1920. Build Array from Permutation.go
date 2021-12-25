package main

import "fmt"

func main() {

	arr := []int{0, 2, 1, 5, 3, 4}
	result := buildArrayPermutation(arr)
	fmt.Println(result)
}

func buildArrayPermutation(arr []int) []int {
	result := make([]int, len(arr))
	for key := range arr {
		result[key] = arr[arr[key]]
	}
	return result
}
