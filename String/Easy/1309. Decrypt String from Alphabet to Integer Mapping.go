package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "10#11#12"
	result := freqAlphabets(str)
	fmt.Println(result)
}

func freqAlphabets(s string) string {

	ans, str := "", strings.Split(s, "")
	n := len(str)
	alphabets := map[string]string{
		"1":  "a",
		"2":  "b",
		"3":  "c",
		"4":  "d",
		"5":  "e",
		"6":  "f",
		"7":  "g",
		"8":  "h",
		"9":  "i",
		"10": "j",
		"11": "k",
		"12": "l",
		"13": "m",
		"14": "n",
		"15": "o",
		"16": "p",
		"17": "q",
		"18": "r",
		"19": "s",
		"20": "t",
		"21": "u",
		"22": "v",
		"23": "w",
		"24": "x",
		"25": "y",
		"26": "z",
	}

	for i := 0; i < n; i++ {
		if str[i] >= "1" && str[i] <= "9" && ((i+2 < n && str[i+2] != "#") || (i == n-1 || i == n-2)) {
			val := alphabets[str[i]]
			ans += val
		} else if i+1 < n && str[i]+str[i+1] >= "10" && i+2 < n && str[i+2] == "#" {
			val := alphabets[str[i]+str[i+1]]
			ans += val
			i += 2
		}
	}
	return ans
}
