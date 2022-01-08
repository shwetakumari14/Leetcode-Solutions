package main

import "fmt"

func main() {

	arr, k := []string{"d", "b", "c", "b", "c", "a"}, 2
	result := kthDistinct(arr, k)
	fmt.Println(result)
}

func kthDistinct(arr []string, k int) string {

	ans := ""

	ansMap := make(map[string]int)
	for _, val := range arr {
		ansMap[val]++
	}

	for i := 0; i < len(arr); i++ {
		val, ok := ansMap[arr[i]]
		if ok && val == 1 && k > 0 {
			ans = arr[i]
			k--
		}
	}

	if k == 0 {
		return ans
	}
	return ""
}
