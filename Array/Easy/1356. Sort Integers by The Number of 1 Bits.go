package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

func main() {

	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8}
	result := sortByBits(arr)
	fmt.Println(result)
}

func sortByBits(arr []int) []int {
	sort.Slice(arr, func(i, j int) bool {
		x, y := oneCount(arr[i]), oneCount(arr[j])
		if x == y {
			return arr[i] < arr[j]
		}
		return x < y
	})
	return arr
}

func oneCount(num int) int {
	return strings.Count(strconv.FormatInt(int64(num), 2), "1")
}
