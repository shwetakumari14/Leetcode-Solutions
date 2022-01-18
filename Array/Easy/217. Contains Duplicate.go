package main

import "fmt"

func main() {

	arr := []int{1, 2, 3, 1}
	result := containsDuplicate(arr)
	fmt.Println(result)
}

func containsDuplicate(nums []int) bool {
	ansMap := make(map[int]int)

	for _, val := range nums {
		_, ok := ansMap[val]
		if ok {
			return true
		}
		ansMap[val]++
	}

	return false
}
