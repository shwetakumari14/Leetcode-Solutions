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

	for i := 0; i < len(str)/2; i++ {
		if str[i] != str[len(str)-1-i] {
			return false
		}
	}

	return true
}
