package main

import (
	"fmt"
	"math/rand"
)

func main() {

	n := 4
	result := sumZero(n)
	fmt.Println(result)
}

func sumZero(n int) []int {
	var arr []int
	ansMap := make(map[int]int)

	if n%2 == 0 {
		for n > 0 {
			positive := rand.Intn(1000)
			if positive != 0 {
				negative := -positive
				_, ok := ansMap[positive]
				if !ok {
					ansMap[positive]++
					ansMap[negative]++
					n -= 2
				}
			}
		}
	} else {
		for n > 1 {
			positive := rand.Intn(1000)
			if positive != 0 {
				negative := -positive
				_, ok := ansMap[positive]
				if !ok {
					ansMap[positive]++
					ansMap[negative]++
					n -= 2
				}
			}
		}
	}
	for key := range ansMap {
		arr = append(arr, key)
	}

	if n%2 == 1 {
		arr = append(arr, 0)
	}

	return arr
}
