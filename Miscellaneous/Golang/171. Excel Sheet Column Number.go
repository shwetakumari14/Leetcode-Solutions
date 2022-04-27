package main

import "fmt"

func main() {

	columnTitle := "AA"
	result := titleToNumber(columnTitle)
	fmt.Println(result)
}

func titleToNumber(columnTitle string) int {
	ans := 0

	for i := 0; i < len(columnTitle); i++ {
		ans = ans*26 + int(columnTitle[i]) - 64
	}

	return ans
}
