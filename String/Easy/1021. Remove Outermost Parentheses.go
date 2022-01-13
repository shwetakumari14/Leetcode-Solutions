package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "(()())(())"
	result := removeOuterParentheses(str)
	fmt.Println(result)
}

func removeOuterParentheses(s string) string {
	str, tempStr, result := strings.Split(s, ""), "", ""
	var temp []string
	for i := 0; i < len(str); i++ {
		if str[i] == "(" {
			temp = append(temp, str[i])
			tempStr += str[i]
		}
		if str[i] == ")" {
			temp = temp[:len(temp)-1]
			tempStr += str[i]
			if len(temp) == 0 {
				result += tempStr[1 : len(tempStr)-1]
				tempStr = ""
			}
		}
	}

	return result
}
