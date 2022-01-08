package main

import "fmt"

func main() {

	n := 6
	result := generateTheString(n)
	fmt.Println(result)

}

func generateTheString(n int) string {

	ans := ""
	if n%2 == 0 {
		for n > 1 {
			ans += "a"
			n--
		}
		ans += "b"
	} else {
		for n > 0 {
			ans += "a"
			n--
		}
	}

	return ans
}
