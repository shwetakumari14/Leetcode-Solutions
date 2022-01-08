package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "bbb"
	result := checkString1(str)
	fmt.Println(result)
}

func checkString(s string) bool {

	str := strings.Split(s, "")
	ansMap := make(map[string]int)
	for _, val := range str {
		ansMap[val]++
	}

	for i := 0; i < len(str); i++ {
		if str[i] == "a" {
			ansMap["a"]--
		}
		if str[i] == "b" {
			val := ansMap["a"]
			if val == 0 {
				continue
			} else {
				return false
			}
		}
	}

	return true
}

func checkString1(s string) bool {

	str := strings.Split(s, "")

	for i := 0; i < len(str)-1; i++ {
		if str[i] == "b" && str[i+1] == "a" {
			return false
		}
	}

	return true
}
