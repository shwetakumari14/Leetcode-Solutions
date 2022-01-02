package main

import (
	"fmt"
)

func main() {

	encoded, first := []int{6, 2, 7, 3}, 4
	result := decode(encoded, first)
	fmt.Println(result)
}

func decode(encoded []int, first int) []int {
	ans := make([]int, len(encoded)+1)
	ans[0] = first

	for i := 0; i < len(encoded); i++ {
		ans[i+1] = encoded[i] ^ ans[i]
	}

	return ans
}
