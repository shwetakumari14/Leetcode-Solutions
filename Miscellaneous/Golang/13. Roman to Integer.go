package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "IX"
	result := romanToInt(str)
	fmt.Println(result)
}

func romanToInt(s string) int {
	str := strings.Split(s, "")
	res := 0

	for i := 0; i < len(str); i++ {
		str1 := charToInt(str[i])
		if i+1 < len(str) {
			str2 := charToInt(str[i+1])
			if str2 <= str1 {
				res += str1
			} else {
				res += str2
				res -= str1
				i++
			}
		} else {
			res += str1
		}
	}

	return res
}

func charToInt(s string) int {
	var num int

	switch s {
	case "I":
		num = 1
		break
	case "V":
		num = 5
		break
	case "X":
		num = 10
		break
	case "L":
		num = 50
		break
	case "C":
		num = 100
		break
	case "D":
		num = 500
		break
	case "M":
		num = 1000
		break
	}
	return num
}
