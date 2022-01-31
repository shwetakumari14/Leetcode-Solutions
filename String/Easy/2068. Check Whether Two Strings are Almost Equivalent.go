package main

import (
	"fmt"
	"math"
	"strings"
)

func main() {

	word1, word2 := "aaaa", "aaaa"
	//word1, word2 := "zzzyyy", "iiiiii"
	result := checkAlmostEquivalent(word1, word2)
	fmt.Println(result)
}

func checkAlmostEquivalent(word1 string, word2 string) bool {
	alphabets := make([]int, 26)

	for _, val := range word1 {
		alphabets[val-'a']++
	}
	for _, val := range word2 {
		alphabets[val-'a']--
	}

	for _, val := range alphabets {
		if math.Abs(float64(val)) > 3 {
			return false
		}
	}

	return true
}

func checkAlmostEquivalent2(word1 string, word2 string) bool {
	str1, str2 := strings.Split(word1, ""), strings.Split(word2, "")
	mapWord1, mapWord2, ansMap := make(map[string]int), make(map[string]int), make(map[string]int)

	for _, val := range str1 {
		mapWord1[val]++
	}
	for _, val := range str2 {
		mapWord2[val]++
	}

	for key, val1 := range mapWord1 {
		val2, ok := mapWord2[key]
		_, ok2 := ansMap[key]
		if ok && !ok2 {
			ansMap[key] = int(math.Abs(float64(val2) - float64(val1)))
		} else if !ok2 {
			ansMap[key] = val1
		}
	}

	for key, val1 := range mapWord2 {
		val2, ok := mapWord1[key]
		_, ok2 := ansMap[key]
		if ok && !ok2 {
			ansMap[key] = int(math.Abs(float64(val2) - float64(val1)))
		} else if !ok2 {
			ansMap[key] = val1
		}
	}

	for _, val := range ansMap {
		if val > 3 {
			return false
		}
	}

	return true
}
