package main

import (
	"fmt"
	"strconv"
)

func main() {

	//s, k := "leetcode", 2
	s, k := "fleyctuuajsr", 5
	result := getLucky(s, k)
	fmt.Println(result)
}

func getLucky(s string, k int) int {

	ans, tmp := 0, ""
	for _, val := range s {
		tmp += strconv.Itoa(int(val-'a') + 1)
	}

	for k > 0 {
		temp := 0
		for _, val := range tmp {
			temp += int(val - '0')
		}
		tmp = strconv.Itoa(temp)
		ans = temp
		k--
	}

	return ans

}
