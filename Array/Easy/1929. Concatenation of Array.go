package main

import "fmt"

func main() {

	arr := []int{1, 3, 2, 1}
	result := concatenateArray(arr)
	fmt.Println(result)
}

func concatenateArray(arr []int) []int {
	ans := arr
	ans = append(ans, arr...)

	return ans
}
