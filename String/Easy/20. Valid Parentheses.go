package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "{[(]}"
	result := isValid(str)
	fmt.Println(result)
}

func isValid(s string) bool {
	str, temp := strings.Split(s, ""), ""
	var stack []string

	for i := 0; i < len(str); i++ {
		if str[i] == "(" || str[i] == "[" || str[i] == "{" {
			stack = append(stack, str[i])
			continue
		}
		if len(stack) == 0 {
			return false
		}
		switch str[i] {
		case ")":
			temp = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if temp != "(" {
				return false
			}
			break
		case "]":
			temp = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if temp != "[" {
				return false
			}
			break
		case "}":
			temp = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if temp != "{" {
				return false
			}
			break
		}
	}
	if len(stack) == 0 {
		return true
	}
	return false
}
