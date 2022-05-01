package main

import "fmt"

func main() {

	n := 15
	result := fizzBuzz(n)
	fmt.Println(result)
}

func fizzBuzz(n int) []string {
	var ans []string

	for i := 1; i <= n; i++ {
		if i%3 == 0 && i%5 == 0 {
			ans = append(ans, "\"FizzBuzz\"")
		} else if i%3 == 0 {
			ans = append(ans, "\"Fizz\"")
		} else if i%5 == 0 {
			ans = append(ans, "\"Buzz\"")
		} else {
			temp := fmt.Sprintf("\"%d\"", i)
			ans = append(ans, temp)
		}
	}

	return ans
}
