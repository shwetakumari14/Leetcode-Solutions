package main

import (
	"fmt"
	"strings"
)

func main() {

	patterns, word := []string{"a", "abc", "bc", "d"}, "abc"
	result := numOfStrings(patterns, word)
	fmt.Println(result)

}

func numOfStrings(patterns []string, word string) int {

	count := 0
	for _, pattern := range patterns {
		if strings.Contains(word, pattern) {
			count++
		}
	}

	return count

}
