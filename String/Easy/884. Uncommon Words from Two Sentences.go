package main

import (
	"fmt"
	"strings"
)

func main() {

	s1, s2 := "this apple is sweet", "this apple is sour"
	result := uncommonFromSentences(s1, s2)
	fmt.Println(result)
}

func uncommonFromSentences(s1 string, s2 string) []string {
	str1, str2 := strings.Split(s1, " "), strings.Split(s2, " ")
	strMap1, strMap2 := make(map[string]int), make(map[string]int)

	var ans []string
	for _, val := range str1 {
		strMap1[val]++
	}
	for _, val := range str2 {
		strMap2[val]++
	}

	for key, val := range strMap1 {
		if val == 1 {
			_, ok := strMap2[key]
			if !ok {
				ans = append(ans, key)
			}
		}
	}

	for key, val := range strMap2 {
		if val == 1 {
			_, ok := strMap1[key]
			if !ok {
				ans = append(ans, key)
			}
		}
	}

	return ans

}
