package main

import "fmt"

func main() {

	arr := []int{2, 5, 1, 3, 4, 7}
	result := shuffleArray(arr, 3)
	fmt.Println(result)
}

func shuffleArray(arr []int, n int) []int {
	ans := make([]int, len(arr))

	for i, j, k := 0, n, 0; i < n && j < len(arr) && k < len(arr); i, j = i+1, j+1 {
		ans[k] = arr[i]
		k++
		ans[k] = arr[j]
		k++
	}

	return ans
}
