package main

import (
	"fmt"
	"strings"
)

func main() {

	str, k := "Hello how are you Contestant", 4
	result := truncateSentence(str, k)
	fmt.Println(result)

}

func truncateSentence(s string, k int) string {

	str := strings.Split(s, " ")
	str = str[:k]
	ans := strings.Join(str, " ")

	return ans
}

func truncateSentence2(s string, k int) string {

	var ans string
	str := strings.Split(s, " ")
	for i := 0; i < k; i++ {
		ans = ans + " " + str[i]
	}

	return ans
}
