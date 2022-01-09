package main

import (
	"fmt"
	"strconv"
)

func main() {

	n := 5
	result := fizzBuzz(n)
	fmt.Println(result)
}

func fizzBuzz(n int) []string {

	var ans []string

	for n > 0 {
		if n%3 == 0 && n%5 == 0 {
			ans = append(ans, "FizzBuzz")
		} else if n%3 == 0 {
			ans = append(ans, "Fizz")
		} else if n%5 == 0 {
			ans = append(ans, "Buzz")
		} else {
			ans = append(ans, strconv.Itoa(n))
		}
		n--
	}

	for i, j := 0, len(ans)-1; i < j; i, j = i+1, j-1 {
		ans[i], ans[j] = ans[j], ans[i]
	}

	return ans
}
