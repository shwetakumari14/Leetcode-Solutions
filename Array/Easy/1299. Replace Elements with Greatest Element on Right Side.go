package main

import "fmt"

func main() {

	arr := []int{17, 18, 5, 4, 6, 1}
	result := replaceElements(arr)
	fmt.Println(result)
}

func replaceElements(arr []int) []int {
	ans, n := make([]int, len(arr)), len(arr)
	ans[n-1] = -1

	counter := arr[n-1]
	for i, j := n-1, n-2; i >= 0 && j >= 0; i, j = i-1, j-1 {
		if arr[i] > counter {
			counter = arr[i]
			ans[j] = counter
		} else {
			ans[j] = counter
		}
	}

	return ans
}
