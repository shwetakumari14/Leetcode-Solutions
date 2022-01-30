package main

import (
	"fmt"
	"math"
)

func main() {

	arr, a, b, c := []int{3, 0, 1, 1, 9, 7}, 7, 2, 3
	result := countGoodTriplets2(arr, a, b, c)
	fmt.Println(result)

}

func countGoodTriplets(arr []int, a int, b int, c int) int {
	count := 0
	for i := 0; i < len(arr); i++ {
		for j := i + 1; j < len(arr); j++ {
			for k := j + 1; k < len(arr); k++ {
				if int(math.Abs(float64(arr[i]-arr[j]))) <= a && int(math.Abs(float64(arr[j]-arr[k]))) <= b && int(math.Abs(float64(arr[i]-arr[k]))) <= c {
					count++
				}
			}
		}
	}

	return count

}

func countGoodTriplets2(arr []int, a int, b int, c int) int {
	count := 0
	i, j, k := 0, 1, 2
	for i < len(arr)-2 {
		if int(math.Abs(float64(arr[i]-arr[j]))) <= a && int(math.Abs(float64(arr[j]-arr[k]))) <= b && int(math.Abs(float64(arr[i]-arr[k]))) <= c {
			count++
		}
		if k != len(arr)-1 && j != len(arr)-2 {
			k++
		} else if k == len(arr)-1 && j != len(arr)-2 {
			j++
			k = j + 1
		} else if k != len(arr)-1 && j == len(arr)-2 {
			k++
		} else {
			i++
			j = i + 1
			k = j + 1
		}
	}

	return count

}
