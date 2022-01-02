package main

import "fmt"

func main() {
	jewels, stones := "aA", "aAAbbb"
	result := numJewelsInStones(jewels, stones)
	fmt.Println(result)
}

func numJewelsInStones(jewels string, stones string) int {

	count := 0

	for i := 0; i < len(stones); i++ {
		for j := 0; j < len(jewels); j++ {
			if stones[i] == jewels[j] {
				count++
			}
		}
	}

	return count
}

func numJewelsInStones1(jewels string, stones string) int {

	count := 0
	stonesMap := make(map[rune]int)

	for _, val := range stones {
		stonesMap[val] += 1
	}

	for _, val := range jewels {
		jewel, ok := stonesMap[val]
		if ok {
			count = count + jewel
		}
	}

	return count
}
