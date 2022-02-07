package main

import (
	"fmt"
	"math"
)

func main() {

	rectangles := [][]int{{5, 8}, {3, 9}, {5, 12}, {16, 5}}
	result := countGoodRectangles(rectangles)
	fmt.Println(result)
}

func countGoodRectangles(rectangles [][]int) int {
	var squareLen []int

	for i := 0; i < len(rectangles); i++ {
		squareLen = append(squareLen, min(rectangles[i][0], rectangles[i][1]))
	}

	maxLen, count := math.MinInt, 0

	for i := 0; i < len(squareLen); i++ {
		if maxLen < squareLen[i] {
			maxLen = squareLen[i]
		}
	}

	for i := 0; i < len(squareLen); i++ {
		if maxLen == squareLen[i] {
			count++
		}
	}

	return count

}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
