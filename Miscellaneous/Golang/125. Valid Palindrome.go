package main

import (
	"fmt"
	"regexp"
	"strings"
)

func main() {

	str := "A man, a plan, a canal: Panama"
	result := isPalindrome(str)
	fmt.Println(result)
}

func isPalindrome(s string) bool {
	reg, _ := regexp.Compile("[^a-zA-Z0-9]+")
	str := reg.ReplaceAllString(s, "")
	str = strings.ToLower(str)

	n := len(str)

	for i := 0; i < n; i++ {
		if str[i] != str[n-1-i] {
			return false
		}
	}

	return true
}
