package main

import (
	"fmt"
	"strings"
)

func main() {

	sentence := "hequickbrownfoxjumpsoverthelazydog"
	result := checkIfPangram(sentence)
	fmt.Println(result)
}

func checkIfPangram(sentence string) bool {

	alphabetMap := make(map[string]int)

	str := strings.Split(sentence, "")
	for _, letter := range str {
		alphabetMap[letter]++
	}

	if len(alphabetMap) == 26 {
		return true
	}

	return false
}
