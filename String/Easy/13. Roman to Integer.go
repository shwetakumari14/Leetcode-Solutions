package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "MCMXCIV"
	result := romanToInt(str)
	fmt.Println(result)
}

func romanNum(str string) int {
	switch str {
	case "I":
		return 1
	case "V":
		return 5
	case "X":
		return 10
	case "L":
		return 50
	case "C":
		return 100
	case "D":
		return 500
	case "M":
		return 1000
	}
	return 0
}

func romanToInt(s string) int {
	str := strings.Split(s, "")
	result, x, y := 0, 0, 0

	for i := 0; i < len(str); i++ {
		x = romanNum(str[i])
		if i+1 < len(str) {
			y = romanNum(str[i+1])
			if x >= y {
				result += x
			} else {
				result += y
				result -= x
				i++
			}
		} else {
			result += x
		}
	}

	return result
}
