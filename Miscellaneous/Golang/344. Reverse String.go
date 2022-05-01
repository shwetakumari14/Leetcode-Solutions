package main

import "fmt"

func main() {

	str := []string{"H", "a", "n", "n", "a", "h"}
	result := reverseString(str)
	fmt.Println(result)
}

func reverseString(str []string) []string {
	for i, j := 0, len(str)-1; i < j; i, j = i+1, j-1 {
		str[i], str[j] = str[j], str[i]
	}
	return str
}
