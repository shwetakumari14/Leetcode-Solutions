package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "xyzzaz"
	result := countGoodSubstrings(str)
	fmt.Println(result)
}

func countGoodSubstrings(s string) int {
	str := strings.Split(s, "")
	count := 0

	if len(str) == 1 {
		return 0
	} else if len(str) == 2 {
		if str[0] == str[1] {
			return 0
		} else {
			return 1
		}
	} else {
		for i, j, k := 0, 1, 2; i < j && j < k && k < len(str); i, j, k = i+1, j+1, k+1 {
			if str[i] != str[j] && str[j] != str[k] && str[k] != str[i] {
				count++
			}
		}
	}

	return count
}
