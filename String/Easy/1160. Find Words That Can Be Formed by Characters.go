package main

import (
	"fmt"
	"strings"
)

func main() {

	words, chars := []string{"hello", "world", "leetcode"}, "welldonehoneyr"
	result := countCharacters(words, chars)
	fmt.Println(result)
}

func countCharacters(words []string, chars string) int {
	charStr := strings.Split(chars, "")
	charMap := make(map[string]int)

	var ans string

	for _, val := range charStr {
		charMap[val]++
	}

	for _, val := range words {
		var temp string
		str := strings.Split(val, "")
		tempMap := make(map[string]int)
		for tempkey, tempVal := range charMap {
			tempMap[tempkey] = tempVal
		}

		for _, char := range str {
			value, ok := tempMap[char]
			if ok && value > 0 {
				temp += char
				tempMap[char]--
			} else {
				temp = ""
				break
			}
		}
		ans += temp
	}

	return len(ans)
}
