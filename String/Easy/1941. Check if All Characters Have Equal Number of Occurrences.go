package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "abacbc"
	result := areOccurrencesEqual(str)
	fmt.Println(result)
}

func areOccurrencesEqual(s string) bool {
	str := strings.Split(s, "")
	ansMap := make(map[string]int)
	for _, val := range str {
		ansMap[val]++
	}

	var result []int

	for _, val := range ansMap {
		result = append(result, val)
	}

	for i := 0; i < len(result)-1; i++ {
		if result[i] != result[i+1] {
			return false
		}
	}

	return true
}
