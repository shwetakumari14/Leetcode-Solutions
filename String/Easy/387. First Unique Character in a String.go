package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "leetcode"
	result := firstUniqChar(str)
	fmt.Println(result)
}

func firstUniqChar(s string) int {
	str := strings.Split(s, "")
	ansMap := make(map[string]int)

	for _, val := range str {
		ansMap[val]++
	}

	for key, val := range str {
		val, ok := ansMap[val]
		if ok && val == 1 {
			return key
		}
	}
	return -1
}
