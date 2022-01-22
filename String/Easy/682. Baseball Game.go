package main

import (
	"fmt"
	"strconv"
)

func main() {

	ops := []string{"5", "2", "C", "D", "+"}
	result := calPoints(ops)
	fmt.Println(result)
}

func calPoints(ops []string) int {
	sum := 0
	var ans []int
	temp, _ := strconv.Atoi(ops[0])
	ans = append(ans, temp)
	for i := 1; i < len(ops); i++ {
		if ops[i] == "C" {
			ans = ans[:len(ans)-1]
		} else if ops[i] == "+" {
			ans = append(ans, ans[len(ans)-1]+ans[len(ans)-2])
		} else if ops[i] == "D" {
			ans = append(ans, 2*ans[len(ans)-1])
		} else {
			temp1, _ := strconv.Atoi(ops[i])
			ans = append(ans, temp1)
		}
	}

	for _, val := range ans {
		sum += val
	}

	return sum

}
