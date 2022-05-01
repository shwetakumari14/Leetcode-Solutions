package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "loveleetcode"
	result := uniqueChar(str)
	fmt.Println(result)
}

func uniqueChar(s string) int {
	str := strings.Split(s, "")
	ansMap := make(map[string]int)

	for _, char := range str {
		ansMap[char]++
	}

	for i := 0; i < len(str); i++ {
		val, ok := ansMap[str[i]]
		if ok && val == 1 {
			return i
		}
	}

	return -1
}
