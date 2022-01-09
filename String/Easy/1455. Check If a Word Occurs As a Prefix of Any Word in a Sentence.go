package main

import (
	"fmt"
	"strings"
)

func main() {

	sentence, searchWord := "i love eating burger", "burg"
	result := isPrefixOfWord(sentence, searchWord)
	fmt.Println(result)

}

func isPrefixOfWord(sentence string, searchWord string) int {
	str := strings.Split(sentence, " ")

	for i := 0; i < len(str); i++ {
		if strings.HasPrefix(str[i], searchWord) {
			return i + 1
		}
	}

	return -1
}
