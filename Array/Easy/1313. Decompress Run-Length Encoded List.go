package main

import "fmt"

func main() {

	arr := []int{1, 1, 2, 3}
	result := decompressRLElist(arr)
	fmt.Println(result)
}

func decompressRLElist(arr []int) []int {
	var ans []int

	for i := 0; i < len(arr); i = i + 2 {
		freq := arr[i]
		for freq > 0 {
			ans = append(ans, arr[i+1])
			freq--
		}
	}

	return ans
}
