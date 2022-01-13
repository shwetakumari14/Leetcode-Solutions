package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "RLRRLLRLRL"
	result := balancedStringSplit(str)
	fmt.Println(result)
}

func balancedStringSplit(s string) int {
	count, str := 0, strings.Split(s, "")

	temp := str[0]
	for i := 1; i < len(str); i++ {
		temp += str[i]
		if isBalanced(temp) {
			count++
		}
	}

	return count
}

func isBalanced(s string) bool {
	rCount, lCount, str := 0, 0, strings.Split(s, "")
	for _, val := range str {
		if val == "R" {
			rCount++
		} else if val == "L" {
			lCount++
		}
	}

	if rCount == lCount {
		return true
	}

	return false
}
