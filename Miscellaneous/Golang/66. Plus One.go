package main

import "fmt"

func main() {

	arr := []int{1, 2, 3}
	result := plusOne(arr)
	fmt.Println(result)
}

func plusOne(num []int) []int {
	var temp, ans []int
	carry := 1

	for i := len(num) - 1; i >= 0; i-- {
		sum := num[i] + carry
		carry = sum / 10
		temp = append(temp, sum%10)
	}
	if carry > 0 {
		temp = append(temp, carry)
	}

	idx := len(temp) - 1
	for i := 0; i < len(temp); i++ {
		if temp[i] == 0 {
			idx--
		}
	}

	for i := idx; i >= 0; i-- {
		ans = append(ans, temp[i])
	}

	return ans
}
