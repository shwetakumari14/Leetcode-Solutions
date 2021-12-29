package main

import "fmt"

func main() {

	arr := [][]int{{2, 8, 7}, {7, 1, 3}, {1, 9, 5}}
	result := maxWealth(arr)
	fmt.Println(result)
}

func maxWealth(arr [][]int) int {
	maxWealth := 0
	for _, customer := range arr {
		eachCustomerWealth := 0
		for _, wealth := range customer {
			eachCustomerWealth += wealth
		}
		if maxWealth < eachCustomerWealth {
			maxWealth = eachCustomerWealth
		}
	}

	return maxWealth
}
