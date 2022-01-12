package main

import (
	"fmt"
	"strings"
)

func main() {

	words := []string{"Hello", "Alaska", "Dad", "Peace"}
	result := findWords(words)
	fmt.Println(result)
}

func findWords(words []string) []string {
	keyboardKeys := []string{"qwertyuiop", "asdfghjkl", "zxcvbnm"}
	var ans []string

	for key, word := range words {
		word = strings.ToLower(word)

		temp := ""
		for _, row := range keyboardKeys {
			for _, ok := range word {
				if strings.ContainsRune(row, ok) {
					temp += string(ok)
				} else {
					break
				}
			}
		}
		if len(temp) == len(word) {
			ans = append(ans, words[key])
		}
	}
	return ans
}
