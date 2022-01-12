package main

import (
	"fmt"
	"strconv"
)

func main() {

	num := 121
	result := isPalindrome(num)
	fmt.Println(result)
}

func isPalindrome(x int) bool {
	str := strconv.Itoa(x)

	for i := 0; i < len(str)/2; i++ {
		if str[i] != str[len(str)-1-i] {
			return false
		}
	}
	return true
}
