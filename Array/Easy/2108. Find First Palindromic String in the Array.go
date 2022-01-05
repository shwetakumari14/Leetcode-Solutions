package main

import "fmt"

func main() {

	words := []string{"abc", "car", "ada", "racecar", "cool"}
	result := firstPalindrome(words)
	fmt.Println(result)
}

func firstPalindrome(words []string) string {

	for _, word := range words {
		if isPalindrome(word) {
			return word
		}
	}

	return ""
}

func isPalindrome(str string) bool {
	n := len(str)
	for i := 0; i < n/2; i++ {
		if str[i] != str[n-i-1] {
			return false
		}
	}

	return true
}
