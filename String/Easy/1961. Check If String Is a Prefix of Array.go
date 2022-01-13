package main

import (
	"fmt"
	"strings"
)

func main() {

	s, words := "iloveleetcode", []string{"i", "love", "leetcode", "apples"}
	result := isPrefixString(s, words)
	fmt.Println(result)
}

func isPrefixString(s string, words []string) bool {
	temp := ""

	for _, word := range words {
		temp += word
		if temp == s {
			return true
		}
		if !strings.Contains(s, temp) {
			return false
		}
	}
	return false
}
