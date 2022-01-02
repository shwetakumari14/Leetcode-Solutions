package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	str := "is2 sentence4 This1 a3"
	result := sortSentence(str)
	fmt.Println(result)
}

func sortSentence(s string) string {
	str := strings.Split(s, " ")
	ansMap := make(map[int]string)
	tempAns := make([]string, len(str))

	for _, val := range str {
		smallStr := strings.Split(val, "")
		key, _ := strconv.Atoi(smallStr[len(smallStr)-1])
		tempArray := smallStr[:len(smallStr)-1]
		tempStr := strings.Join(tempArray, "")
		ansMap[key] = tempStr
	}

	for i := 0; i < len(str); i++ {
		tempAns[i] = ansMap[i+1]
	}
	ans := strings.Join(tempAns, " ")

	return ans
}
