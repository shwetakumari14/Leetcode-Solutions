package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "PPALLP"
	result := checkRecord(str)
	fmt.Println(result)
}

func checkRecord(s string) bool {
	str := strings.Split(s, "")
	aCount := 0
	for i := 0; i < len(str); i++ {
		if str[i] == "A" {
			aCount++
			if aCount > 1 {
				return false
			}
		}

		if i < len(str)-2 && str[i] == "L" && str[i+1] == "L" && str[i+2] == "L" {
			return false
		}
	}
	return true
}
