package main

import "fmt"

func main() {

	num1, num2 := []int{1, 2, 2, 1}, []int{2, 2}
	result := intersection(num1, num2)
	fmt.Println(result)
}

func intersection(nums1 []int, nums2 []int) []int {
	var ans []int
	num1Map, num2Map := make(map[int]int), make(map[int]int)

	for _, val := range nums1 {
		num1Map[val]++
	}

	for _, val := range nums2 {
		num2Map[val]++
	}

	for key := range num1Map {
		_, ok := num2Map[key]
		if ok {
			ans = append(ans, key)
		}
	}

	return ans
}
