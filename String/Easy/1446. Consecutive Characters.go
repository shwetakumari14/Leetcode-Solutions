package main

import (
	"fmt"
	"strings"
)

func main() {

	s := "abbcccddddeeeeedcba"
	//s := "bacacccbba"
	result := maxPower(s)
	fmt.Println(result)
}

func maxPower(s string) int {
	str, st, end, prev, res := strings.Split(s, ""), 0, 0, 0, 0

	for i := 0; i < len(str)-1; i++ {
		if str[i] == str[i+1] {
			if prev == 0 {
				st = i
				prev++
			}
			end = i + 1
		} else {
			prev = 0
		}

		res = max(res, end-st+1)
	}

	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
