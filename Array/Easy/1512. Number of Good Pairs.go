package main

import "fmt"

func main() {

	arr := []int{1, 1, 1, 1}
	//noOfGoodPairs := numIdenticalPairs2(arr)
	noOfGoodPairs := numIdenticalPairs2(arr)
	fmt.Println(noOfGoodPairs)
}

func numIdenticalPairs(arr []int) int {
	ans := 0

	for i := 0; i < len(arr); i++ {
		for j := i + 1; j < len(arr); j++ {
			if arr[i] == arr[j] && i < j {
				ans += 1
			}
		}
	}

	return ans
}

func numIdenticalPairs2(arr []int) int {
	ans := 0
	nums := make(map[int]int)

	for _, val := range arr {
		nums[val] += 1
	}

	for _, val := range nums {
		ans += val * (val - 1) / 2
	}

	return ans
}
