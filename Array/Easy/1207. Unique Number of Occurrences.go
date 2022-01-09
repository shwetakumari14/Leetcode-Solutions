package main

import "fmt"

func main() {

	arr := []int{1, 2, 2, 1, 1, 3}
	result := uniqueOccurrences(arr)
	fmt.Println(result)
}

func uniqueOccurrences(arr []int) bool {
	counterMap, ansMap := make(map[int]int), make(map[int]int)

	for _, val := range arr {
		counterMap[val]++
	}

	for _, val := range counterMap {
		_, ok := ansMap[val]
		if ok {
			return false
		}
		ansMap[val]++
	}

	return true
}
