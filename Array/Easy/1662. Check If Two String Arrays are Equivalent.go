package main

import (
	"fmt"
	"strings"
)

func main() {

	word1, word2 := []string{"ab", "c"}, []string{"a", "bc"}
	result := arrayStringsAreEqual(word1, word2)
	fmt.Println(result)

}

func arrayStringsAreEqual(word1 []string, word2 []string) bool {

	str1 := strings.Join(word1, "")
	str2 := strings.Join(word2, "")

	if str1 == str2 {
		return true
	}

	return false
}
