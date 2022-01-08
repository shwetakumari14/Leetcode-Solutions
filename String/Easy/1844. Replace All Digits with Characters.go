package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {

	str := "a1b2c3d4e"
	result := replaceDigits1(str)
	fmt.Println(result)

}

const abc = "abcdefghijklmnopqrstuvwxyz"

func toCharStrConst(i int) string {
	return abc[i-1 : i]
}

func replaceDigits(s string) string {
	str := strings.Split(s, "")
	alphabets := map[string]int{
		"a": 1,
		"b": 2,
		"c": 3,
		"d": 4,
		"e": 5,
		"f": 6,
		"g": 7,
		"h": 8,
		"i": 9,
		"j": 10,
		"k": 11,
		"l": 12,
		"m": 13,
		"n": 14,
		"o": 15,
		"p": 16,
		"q": 17,
		"r": 18,
		"s": 19,
		"t": 20,
		"u": 21,
		"v": 22,
		"w": 23,
		"x": 24,
		"y": 25,
		"z": 26,
	}

	ans := ""

	for i := 0; i < len(str); i++ {
		if i+1 < len(str) {
			val := alphabets[str[i]]
			num, _ := strconv.Atoi(str[i+1])
			ans += str[i] + toCharStrConst(val+num)
			i++
		} else {
			ans += str[i]
		}
	}

	return ans
}

func replaceDigits1(s string) string {
	ans := []byte(s)
	for i := 1; i < len(s); i += 2 {
		ans[i] = ans[i-1] + ans[i] - '0'
	}
	return string(ans)
}
