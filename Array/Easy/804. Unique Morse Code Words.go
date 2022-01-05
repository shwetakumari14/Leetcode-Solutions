package main

import (
	"fmt"
	"strings"
)

func main() {

	words := []string{"zocd", "gjkl", "hzqk", "hzgq", "gjkl"}
	result := uniqueMorseRepresentations(words)
	fmt.Println(result)

}

func uniqueMorseRepresentations(words []string) int {

	ansMap := make(map[string]int)
	morseAlphabet := map[string]string{
		"a": ".-",
		"b": "-...",
		"c": "-.-.",
		"d": "-..",
		"e": ".",
		"f": "..-.",
		"g": "--.",
		"h": "....",
		"i": "..",
		"j": ".---",
		"k": "-.-",
		"l": ".-..",
		"m": "--",
		"n": "-.",
		"o": "---",
		"p": ".--.",
		"q": "--.-",
		"r": ".-.",
		"s": "...",
		"t": "-",
		"u": "..-",
		"v": "...-",
		"w": ".--",
		"x": "-..-",
		"y": "-.--",
		"z": "--..",
	}

	for _, word := range words {
		str := strings.Split(word, "")
		tempStr1 := ""
		for _, val := range str {
			tempStr1 += morseAlphabet[val]
		}
		ansMap[tempStr1] += 1
	}

	return len(ansMap)
}
