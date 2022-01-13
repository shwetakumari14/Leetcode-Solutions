package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {

	str := "dfa12321afd"
	result := secondHighest(str)
	fmt.Println(result)
}

func secondHighest(s string) int {
	str, max1, max2 := strings.Split(s, ""), 0, 0
	var arr []int

	for i := 0; i < len(str); i++ {
		if str[i] >= "0" && str[i] <= "9" {
			val, _ := strconv.Atoi(str[i])
			arr = append(arr, val)
		}
	}

	if len(arr) > 0 {
		max1 = arr[0]
		for i := 1; i < len(arr)-1; i++ {
			if max1 < arr[i] {
				max2 = max1
				max2 = arr[i]
			} else if max2 < arr[i] {
				max2 = arr[i]
			}
		}
	}

	if max1 == max2 {
		return -1
	}
	return max2
}
