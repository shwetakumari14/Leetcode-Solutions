package main

import (
	"fmt"
	"strings"
)

func main() {

	text, first, second := "alice is a good girl she is a good student", "a", "good"
	result := findOcurrences(text, first, second)
	fmt.Println(result)
}

func findOcurrences(text string, first string, second string) []string {

	var ans []string
	str := strings.Split(text, " ")

	for i := 0; i < len(str)-2; i++ {
		if str[i] == first && str[i+1] == second {
			ans = append(ans, str[i+2])
		}
	}

	return ans
}
