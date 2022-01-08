package main

import "fmt"

func main() {

	var str = []string{"h", "e", "l", "l", "o"}
	result := reverseString(str)
	fmt.Println(result)
}

func reverseString(s []string) []string {

	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
	return s
}
