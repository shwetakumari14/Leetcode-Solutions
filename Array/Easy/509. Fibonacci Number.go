package main

import "fmt"

func main() {

	n := 7
	result := fib(n)
	fmt.Println(result)
}

func fib(n int) int {
	if n == 0 || n == 1 {
		return n
	}

	return fib(n-1) + fib(n-2)
}
