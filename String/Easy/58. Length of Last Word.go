package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "Hello World"
	result := lengthOfLastWord(str)
	fmt.Println(result)
}

func lengthOfLastWord(s string) int {
	s1 := strings.Trim(s, " ")
	count := 0
	for i := len(s1) - 1; i >= 0; i-- {
		if string(s1[i]) == " " {
			return count
		}
		count++
	}
	return count
}
