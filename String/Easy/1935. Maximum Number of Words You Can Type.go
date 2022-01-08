package main

import (
	"fmt"
	"strings"
)

func main() {
	text, brokenLetters := "hello world", "ad"
	result := canBeTypedWords(text, brokenLetters)
	fmt.Println(result)
}

func canBeTypedWords(text string, brokenLetters string) int {
	textStr := strings.Split(text, " ")
	brokenLetter := strings.Split(brokenLetters, "")

	charMap := make(map[string]int)
	count := 0

	for _, val := range brokenLetter {
		charMap[val]++
	}

	for i := 0; i < len(textStr); i++ {
		str := strings.Split(textStr[i], "")
		flag := true
		for _, ch := range str {
			_, ok := charMap[ch]
			if ok {
				flag = false
			}
		}
		if flag {
			count++
		}
	}

	return count
}
