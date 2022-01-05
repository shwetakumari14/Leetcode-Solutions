package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "(1+(2*3)+((8)/4))+1"
	result := maxDepth(str)
	fmt.Println(result)
}

func maxDepth(s string) int {

	count, level := 0, 0
	str := strings.Split(s, "")

	for i := 0; i < len(str); i++ {
		if str[i] == "(" {
			count++
		} else if str[i] == ")" {
			level = max(level, count)
			count--
		}
	}
	return level
}

func max(level, count int) int {
	if level > count {
		return level
	}
	return count
}
