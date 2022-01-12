package main

import (
	"fmt"
	"strings"
)

func main() {

	word := "Google"
	result := detectCapitalUse(word)
	fmt.Println(result)
}

func detectCapitalUse(word string) bool {
	if strings.ToUpper(word) == word {
		return true
	} else if strings.ToLower(word) == word {
		return true
	} else if strings.ToUpper(string(word[0])) == string(word[0]) && strings.ToLower(string(word[1:])) == string(word[1:]) {
		return true
	}

	return false
}
