package main

import (
	"fmt"
)

func main() {

	allowed, words := "ab", []string{"ad", "bd", "aaab", "baa", "badab"}
	result := countConsistentStrings(allowed, words)
	fmt.Println(result)

}

func countConsistentStrings(allowed string, words []string) int {

	count := 0
	ansMap := make(map[rune]int)

	for _, val := range allowed {
		ansMap[val]++
	}

	for _, val1 := range words {
		for _, val2 := range val1 {
			_, ok := ansMap[val2]
			if !ok {
				count++
				break
			}
		}
	}

	return len(words) - count

}
