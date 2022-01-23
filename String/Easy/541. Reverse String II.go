package main

import (
	"fmt"
	"strings"
)

func main() {

	str, k := "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39
	result := reverseStr(str, k)
	fmt.Println(result)
}

func reverseStr(s string, k int) string {
	str := strings.Split(s, "")
	if len(s) <= k {
		return reverseSubString(str, 0, len(s)-1)
	}
	ans := ""
	for i := 0; i < len(str); i += 2 * k {
		if i+(k-1) < len(str) {
			ans = reverseSubString(str, i, i+(k-1))
		} else if i+(k-1) > len(str) {
			ans = reverseSubString(str, i, len(str)-1)
		}
	}
	return ans
}

func reverseSubString(str []string, i, k int) string {
	for i < k {
		str[i], str[k] = str[k], str[i]
		k--
		i++
	}
	return strings.Join(str, "")
}
