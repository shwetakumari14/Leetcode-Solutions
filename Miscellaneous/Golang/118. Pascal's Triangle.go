package main

import "fmt"

func main() {

	result := generate(5)
	fmt.Println(result)
}

func generate(numRows int) [][]int {
	solution := make([][]int, numRows)
	i := 1

	for j := range solution {
		solution[j] = make([]int, i)
		i++
	}

	for i := 0; i < numRows; i++ {
		for j := 0; j <= i; j++ {
			if j == 0 || i == j {
				solution[i][j] = 1
			} else {
				solution[i][j] = solution[i-1][j-1] + solution[i-1][j]
			}
		}
	}

	return solution
}
