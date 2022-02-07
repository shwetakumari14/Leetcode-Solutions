package main

import (
	"fmt"
)

func main() {

	widths, s := []int{4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10}, "bbbcccdddaaa"
	result := numberOfLines(widths, s)
	fmt.Println(result)
}

func numberOfLines(widths []int, s string) []int {
	ans, sum, count := make([]int, 2), 0, 1

	for i := 0; i < len(s); i++ {
		num := int(s[i] - 'a' + 1)
		if sum+widths[num-1] > 100 {
			count++
			sum = widths[num-1]
		} else {
			sum += widths[num-1]

		}
	}

	ans[0] = count
	ans[1] = sum

	return ans
}
