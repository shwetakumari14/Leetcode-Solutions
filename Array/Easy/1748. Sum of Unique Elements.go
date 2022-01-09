package main

import "fmt"

func main() {

	arr := []int{1, 2, 3, 2}
	result := sumOfUnique(arr)
	fmt.Println(result)
}

func sumOfUnique(nums []int) int {

	ansMap, sum := make(map[int]int), 0

	for _, val := range nums {
		ansMap[val]++
	}

	for key, val := range ansMap {
		if val == 1 {
			sum += key
		}
	}

	return sum
}
