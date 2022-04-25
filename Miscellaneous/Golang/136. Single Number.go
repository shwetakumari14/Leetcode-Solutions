package main

import "fmt"

func main() {

	arr := []int{4, 2, 1, 2, 1}
	result := singleNumber(arr)
	fmt.Println(result)
}

func singleNumber(arr []int) int {
	ans := arr[0]

	for i := 1; i < len(arr); i++ {
		ans ^= arr[i]
	}

	return ans
}
