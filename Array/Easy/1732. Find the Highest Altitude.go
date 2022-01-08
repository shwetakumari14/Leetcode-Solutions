package main

import "fmt"

func main() {

	arr := []int{-5, 1, 5, 0, -7}
	result := largestAltitude(arr)
	fmt.Println(result)
}

func largestAltitude(gain []int) int {
	arr := make([]int, len(gain)+1)
	arr[0] = 0
	max := 0

	for i := 0; i < len(gain); i++ {
		arr[i+1] = gain[i] + arr[i]
	}

	for _, val := range arr {
		if val > max {
			max = val
		}
	}

	return max
}
