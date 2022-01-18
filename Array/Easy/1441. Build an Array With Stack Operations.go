package main

import "fmt"

func main() {

	target, n := []int{1, 3}, 3
	result := buildArray(target, n)
	fmt.Println(result)
}

func buildArray(target []int, n int) []string {
	num := 1
	var ans []string

	for i := 0; i < len(target); {
		if num == target[i] {
			ans = append(ans, "Push")
			i++
		} else {
			ans = append(ans, "Push")
			ans = append(ans, "Pop")
		}
		num++
	}

	return ans
}
