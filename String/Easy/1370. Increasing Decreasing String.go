package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {

	//str := "aaaabbbbcccc"
	str := "leetcode"
	result := sortString(str)
	fmt.Println(result)
}

func sortString(s string) string {
	str, ans := strings.Split(s, ""), ""
	ansMap := make(map[string]int)

	for _, val := range str {
		ansMap[val]++
	}

	var keys []string
	for key := range ansMap {
		keys = append(keys, key)
	}
	sort.Strings(keys)

	i := 0
	for i < len(str) {
		for j := 0; j < len(keys) && i < len(str); j++ {
			count, ok := ansMap[keys[j]]
			if ok && count > 0 {
				ans += keys[j]
				ansMap[keys[j]]--
				i++
			}
		}
		for j := len(keys) - 1; j >= 0 && i < len(str); j-- {
			count, ok := ansMap[keys[j]]
			if ok && count > 0 {
				ans += keys[j]
				ansMap[keys[j]]--
				i++
			}
		}
	}

	return ans
}
