package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "codeleet"
	indices := []int{4, 5, 6, 7, 0, 2, 1, 3}
	result := restoreString(str, indices)
	fmt.Println(result)

}

func restoreString(str string, indices []int) string {

	strArray := strings.Split(str, "")
	ans := make([]string, len(strArray))

	for i := 0; i < len(strArray); i++ {
		ans[indices[i]] = strArray[i]
	}

	ansString := strings.Join(ans, "")
	return ansString
}
