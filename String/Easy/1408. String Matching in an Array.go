package main

import (
	"fmt"
	"strings"
)

func main() {

	words := []string{"leetcoder", "leetcode", "od", "hamlet", "am"}
	result := stringMatching(words)
	fmt.Println(result)
}

func stringMatching(words []string) []string {
	var ans []string
	ansMap := make(map[string]int)

	for i := 0; i < len(words); i++ {
		for j := 0; j < len(words); j++ {
			if i != j && strings.Contains(words[i], words[j]) {
				ansMap[words[j]]++
			}
		}
	}

	for key := range ansMap {
		ans = append(ans, key)
	}

	return ans
}
