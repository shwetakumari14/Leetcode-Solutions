package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {

	str := "hello world 5 x 5"
	result := areNumbersAscending(str)
	fmt.Println(result)
}

func areNumbersAscending(s string) bool {
	str := strings.Split(s, " ")
	ans := 0
	for i := 0; i < len(str); i++ {
		if num, err := strconv.Atoi(str[i]); err == nil {
			if num <= ans {
				return false
			} else {
				ans = num
			}
		}
	}

	return true
}
