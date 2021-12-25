package main

import "fmt"

func main() {

	arr := []int{3, 1, 2, 10, 1}
	result := findRunningArraySum(arr)
	fmt.Println(result)
}

func findRunningArraySum(arr []int) []int {
	ans := make([]int, len(arr))
	ans[0] = arr[0]

	for i := 1; i < len(arr); i++ {
		ans[i] = arr[i] + ans[i-1]
	}
	return ans
}
