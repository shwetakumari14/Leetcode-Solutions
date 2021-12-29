package main

import (
	"fmt"
	"strings"
)

func main() {

	sentences := []string{"alice and bob love leetcode", "i think so too", "this is great thanks very much"}
	maxWords := mostWordsFound(sentences)
	fmt.Println(maxWords)
}

func mostWordsFound(sentences []string) int {
	maxWords := 0

	for _, val := range sentences {
		eachSentence := strings.Split(val, " ")
		tempWordCount := len(eachSentence)
		if maxWords < tempWordCount {
			maxWords = tempWordCount
		}
	}
	return maxWords
}
