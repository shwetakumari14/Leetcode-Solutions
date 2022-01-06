package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "textbook"
	result := halvesAreAlike(str)
	fmt.Println(result)

}

func halvesAreAlike(s string) bool {
	s = strings.ToLower(s)
	str := strings.Split(s, "")
	strlen := len(str)

	firstHalfVowelCount, secondHalfVowelCount := 0, 0

	for i, j := 0, strlen/2; i < strlen/2 && j < strlen; i, j = i+1, j+1 {
		if isVowel(str[i]) {
			firstHalfVowelCount++
		}
		if isVowel(str[j]) {
			secondHalfVowelCount++
		}
	}

	if firstHalfVowelCount == secondHalfVowelCount {
		return true
	}

	return false

}

func isVowel(char string) bool {
	if char == "a" || char == "e" || char == "i" || char == "o" || char == "u" {
		return true
	}
	return false
}
