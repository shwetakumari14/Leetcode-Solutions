package main

import (
	"fmt"
	"strings"
)

func main() {

	rings := "B0B6G0R6R0R6G9"
	result := countPoints(rings)
	fmt.Println(result)
}

func countPoints(rings string) int {
	count := 0

	rodsMap := map[string]map[string]int{
		"0": {"B": 0, "R": 0, "G": 0},
		"1": {"B": 0, "R": 0, "G": 0},
		"2": {"B": 0, "R": 0, "G": 0},
		"3": {"B": 0, "R": 0, "G": 0},
		"4": {"B": 0, "R": 0, "G": 0},
		"5": {"B": 0, "R": 0, "G": 0},
		"6": {"B": 0, "R": 0, "G": 0},
		"7": {"B": 0, "R": 0, "G": 0},
		"8": {"B": 0, "R": 0, "G": 0},
		"9": {"B": 0, "R": 0, "G": 0},
	}

	str := strings.Split(rings, "")

	for i := 0; i < len(str); i += 2 {
		if str[i] == "B" {
			rodsMap[str[i+1]]["B"] += 1
		} else if str[i] == "G" {
			rodsMap[str[i+1]]["G"] += 1
		} else if str[i] == "R" {
			rodsMap[str[i+1]]["R"] += 1
		}
	}

	for _, val := range rodsMap {
		if val["R"] > 0 && val["B"] > 0 && val["G"] > 0 {
			count++
		}
	}

	return count
}
