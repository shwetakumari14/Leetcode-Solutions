package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {

	num := 5
	result := findComplement(num)
	fmt.Println(result)
}

func findComplement(num int) int {

	bin_value := fmt.Sprintf("%b", num)
	val := complementBinary(bin_value)
	ans, _ := strconv.ParseInt(val, 2, 64)

	return int(ans)
}

func complementBinary(s string) string {
	str := strings.Split(s, "")

	for i := 0; i < len(str); i++ {
		if str[i] == "0" {
			str[i] = "1"
		} else if str[i] == "1" {
			str[i] = "0"
		}
	}
	return strings.Join(str, "")
}
