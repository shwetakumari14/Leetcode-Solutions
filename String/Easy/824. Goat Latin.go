package main

import (
	"fmt"
	"strings"
)

func main() {

	sentence := "I speak Goat Latin"
	result := toGoatLatin(sentence)
	fmt.Println(result)
}

func toGoatLatin(sentence string) string {
	ans, str, count := "", strings.Split(sentence, " "), 1

	for i := 0; i < len(str); i++ {
		temp := strings.ToLower(str[i])
		if temp[0] == 'a' || temp[0] == 'e' || temp[0] == 'i' || temp[0] == 'o' || temp[0] == 'u' {
			ans += str[i] + "ma"
		} else {
			temp := str[i]
			ans += string(temp[1:]) + string(temp[0]) + "ma"
		}
		j := 0
		for j < count {
			ans += "a"
			j++
		}
		if i != len(str)-1 {
			ans += " "
		}
		count++
	}

	return ans
}
