package main

import "fmt"

func main() {

	s, t := "anagram", "nagaram"
	result := isValidAnagram(s, t)
	fmt.Println(result)
}

func isValidAnagram(str1, str2 string) bool {

	if len(str1) != len(str2) {
		return false
	}

	count := 0

	for i := 0; i < len(str1); i++ {
		count += int(str1[i])
	}

	for i := 0; i < len(str2); i++ {
		count -= int(str2[i])
	}

	if count == 0 {
		return true
	}
	return false
}
