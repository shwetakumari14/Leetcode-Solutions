package main

import "fmt"

func main() {

	arr := []int{9, 6, 4, 2, 3, 5, 7, 0, 1}
	result := missingNumber(arr)
	fmt.Println(result)
}

func missingNumber(arr []int) int {
	n := len(arr)
	sum := n * (n + 1) / 2

	for _, num := range arr {
		sum -= num
	}
	return sum
}
