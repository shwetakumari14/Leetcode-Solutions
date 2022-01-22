package main

import (
	"fmt"
	"strings"
)

func main() {

	ransomNote, magazine := "aa", "ab"
	result := canConstruct(ransomNote, magazine)
	fmt.Println(result)
}

func canConstruct(ransomNote string, magazine string) bool {
	ransom := strings.Split(ransomNote, "")
	mag := strings.Split(magazine, "")

	ansMap := make(map[string]int)
	for _, val := range mag {
		ansMap[val]++
	}

	for _, val := range ransom {
		count, ok := ansMap[val]
		if !ok || count < 1 {
			return false
		}
		ansMap[val]--
	}
	return true
}
