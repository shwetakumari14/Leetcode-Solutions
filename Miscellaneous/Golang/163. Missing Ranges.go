package main

import (
	"fmt"
	"math"
)

func main() {

	arr, lower, higher := []int{0, 1, 3, 50, 75}, 0, 99
	result := missingRanges(arr, lower, higher)
	fmt.Println(result)
}

func missingRanges(arr []int, lower, higher int) []string {
	var ans []string
	low, up, overFlow := lower, higher, false

	for i := 0; i < len(arr); i++ {
		if low < arr[i] {
			ans = append(ans, getRange(low, arr[i]-1))
		}
		low = arr[i] + 1
		if low == math.MinInt {
			overFlow = true
			break
		}
	}

	if low <= up && !overFlow {
		ans = append(ans, getRange(low, up))
	}

	return ans
}

func getRange(a, b int) string {
	str := ""
	if a == b {
		str = fmt.Sprintf("\"%d\"", a)
	} else {
		str = fmt.Sprintf("\"%d -> %d\"", a, b)
	}

	return str
}
