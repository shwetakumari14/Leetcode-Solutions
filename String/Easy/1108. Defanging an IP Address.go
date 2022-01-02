package main

import (
	"fmt"
	"strings"
)

func main() {

	address := "1.1.1.1"
	result := defangIPaddr1(address)
	fmt.Println(result)
}

func defangIPaddr(address string) string {
	ans := strings.ReplaceAll(address, ".", "[.]")

	return ans
}

func defangIPaddr1(address string) string {
	str := strings.Split(address, "")

	for i := 0; i < len(str); i++ {
		if str[i] == "." {
			str[i] = "[.]"
		}
	}

	ans := strings.Join(str, "")

	return ans
}
