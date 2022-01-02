package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "LOVELY"
	result := toLowerCase(str)
	fmt.Println(result)

}

func toLowerCase(s string) string {
	ans := strings.ToLower(s)

	return ans
}
