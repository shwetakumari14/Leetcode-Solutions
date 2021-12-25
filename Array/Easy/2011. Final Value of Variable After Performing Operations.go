package main

import (
	"fmt"
	"strings"
)

func main() {

	operations := []string{"++X", "++X", "X++"}
	result := performOperation(operations)
	fmt.Println(result)
}

func performOperation(operations []string) int {
	ans := 0

	for _, val := range operations {
		ele := strings.Split(val, "")
		switch ele[1] {
		case "-":
			ans -= 1
		case "+":
			ans += 1
		}
	}
	return ans
}
