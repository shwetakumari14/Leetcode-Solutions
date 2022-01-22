package main

import (
	"fmt"
	"math"
)

func main() {

	num := 28
	result := checkPerfectNumber(num)
	fmt.Println(result)
}

func checkPerfectNumber(num int) bool {
	if num%2 == 1 {
		return false
	}
	sum := 1
	for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
		if num%i == 0 {
			sum += i
			sum += num / i
		}
		if sum > num {
			return false
		}
	}
	if sum == num {
		return true
	}

	return false
}
