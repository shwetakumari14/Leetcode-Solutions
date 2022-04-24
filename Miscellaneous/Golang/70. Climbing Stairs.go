package main

import "fmt"

func main() {

	result := climbStairs2(5)
	fmt.Println(result)
}

func climbStairs1(x int) int {
	result := make([]int, x)
	result[0], result[1] = 1, 2

	for i := 2; i < x; i++ {
		result[i] = result[i-1] + result[i-2]
	}

	return result[len(result)-1]
}

func climbStairs2(x int) int {
	oneStep, twoStep := 1, 2

	for i := 2; i < x; i++ {
		temp := twoStep
		twoStep = oneStep + twoStep
		oneStep = temp
	}

	return twoStep
}
