package main

import (
	"fmt"
	"strings"
)

func main() {

	word1, word2 := "abcd", "pq"
	result := mergeAlternately(word1, word2)
	fmt.Println(result)
}

func mergeAlternately(word1 string, word2 string) string {
	str1, str2 := strings.Split(word1, ""), strings.Split(word2, "")
	i, j := 0, 0
	var ans string
	for i, j = 0, 0; i < len(str1) && j < len(str2); i, j = i+1, j+1 {
		ans += str1[i] + str2[j]
	}

	if i < len(str1) {
		for i < len(str1) {
			ans += str1[i]
			i++
		}
	}

	if j < len(str2) {
		for j < len(str2) {
			ans += str2[j]
			j++
		}
	}

	return ans
}
