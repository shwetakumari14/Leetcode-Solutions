package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {

	firstWord, secondWord, targetWord := "acb", "cba", "cdb"
	result := isSumEqual(firstWord, secondWord, targetWord)
	fmt.Println(result)

}

func isSumEqual(firstWord string, secondWord string, targetWord string) bool {
	firstNum := getNumber(firstWord)
	secondNum := getNumber(secondWord)
	targetNum := getNumber(targetWord)

	if firstNum+secondNum == targetNum {
		return true
	}

	return false
}

func getNumber(str string) int {
	ansMap := map[string]string{"a": "0", "b": "1", "c": "2", "d": "3", "e": "4", "f": "5", "g": "6", "h": "7", "i": "8", "j": "9", "k": "10", "l": "11",
		"m": "12", "n": "13", "o": "14", "p": "15", "q": "16", "r": "17", "s": "18", "t": "19", "u": "20", "v": "21", "w": "22", "x": "23", "y": "24", "z": "25"}
	char := strings.Split(str, "")
	num := ""

	for i := 0; i < len(char); i++ {
		num += ansMap[char[i]]
	}

	ans, _ := strconv.Atoi(num)
	return ans
}
