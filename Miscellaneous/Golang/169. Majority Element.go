package main

import "fmt"

func main() {

	arr := []int{2, 2, 1, 1, 1, 2, 2}
	result := majorityElement(arr)
	fmt.Println(result)
}

func majorityElement(arr []int) int {
	res, times := 0, 0

	for i := 0; i < len(arr); i++ {
		if times == 0 {
			res = arr[i]
		}
		if res == arr[i] {
			times++
		} else {
			times--
		}
	}

	return res
}
