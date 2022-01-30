package main

import (
	"fmt"
	"strings"
)

func main() {

	str, k, fill := "abcdefghik", 3, "x"
	fillByte := []byte(fill)
	result := divideString(str, k, fillByte[0])
	fmt.Println(result)
}

func divideString(s string, k int, fill byte) []string {
	var ans []string
	str := strings.Split(s, "")
	fillStr := string(fill)

	for i := 0; i < len(str); {
		temp := ""
		p := 0
		for p < k && i < len(str) {
			temp = temp + str[i]
			p++
			i++
		}

		if len(temp) < k {
			for len(temp) < k {
				temp = temp + fillStr
			}
		}
		ans = append(ans, temp)
		temp = ""
	}

	return ans
}
