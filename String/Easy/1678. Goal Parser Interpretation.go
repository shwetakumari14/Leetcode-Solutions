package main

import (
	"fmt"
	"strings"
)

func main() {

	command := "G()(al)"
	result := interpret(command)
	fmt.Println(result)
}

func interpret(command string) string {
	str := strings.Split(command, "")
	ans := ""

	for i := 0; i < len(str); i++ {
		if str[i] == "G" {
			ans += str[i]
		} else if str[i] == "(" && str[i+1] == ")" {
			ans += "o"
		} else if str[i] == "(" && str[i+1] == "a" {
			ans += "al"
		}
	}

	return ans
}
