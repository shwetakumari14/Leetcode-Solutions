package main

import "fmt"

func main() {

	arr := []int{1, 2, 3, 1}
	result := containsDuplicate(arr)
	fmt.Println(result)
}

func containsDuplicate(arr []int) bool {
	dict := make(map[int]bool)

	for i := 0; i < len(arr); i++ {
		ok := dict[arr[i]]
		if ok {
			return true
		}
		dict[arr[i]] = true
	}
	return false
}
