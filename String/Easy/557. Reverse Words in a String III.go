package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "Let's take LeetCode contest"
	result := reverseWords(str)
	fmt.Println(result)

}

func reverseWords(s string) string {

	str := strings.Split(s, " ")

	for i := 0; i < len(str); i++ {
		str[i] = reverString(str[i])
	}

	return strings.Join(str, " ")
}

func reverString(s string) string {

	str := strings.Split(s, "")

	for i, j := 0, len(str)-1; i < j; i, j = i+1, j-1 {
		str[i], str[j] = str[j], str[i]
	}

	return strings.Join(str, "")
}
