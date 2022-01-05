package main

import (
	"fmt"
)

func main() {

	arr := []int{1, 4, 2, 5, 3}
	result := sumOddLengthSubarrays2(arr)
	fmt.Println(result)
}

func sumOddLengthSubarrays(arr []int) int {
	oddPointer := 2
	n := len(arr)

	for i := 1; i < n; i++ {
		arr[i] = arr[i] + arr[i-1]
	}
	totalSum := arr[n-1]

	for oddPointer < n {
		for i := 0; i+oddPointer < n; i++ {
			last := i + oddPointer
			if i == 0 {
				totalSum += arr[last]
			} else {
				totalSum += arr[last] - arr[i-1]
			}
		}
		oddPointer += 2
	}

	return totalSum

}

func sumOddLengthSubarrays2(arr []int) int {
	sum, left, right, n := 0, 0, 0, len(arr)

	for left < n {
		for right < n {
			for i := left; i <= right; i++ {
				sum += arr[i]
			}
			right += 2
		}
		left++
		right = left
	}

	return sum
}
