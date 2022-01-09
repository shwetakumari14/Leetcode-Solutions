package main

import "fmt"

func main() {
	mat := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	result := diagonalSum1(mat)
	fmt.Println(result)
}

func diagonalSum(mat [][]int) int {

	sum, n := 0, len(mat[0])

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if i == j || (i+j == n-1) {
				sum += mat[i][j]
			}
		}
	}

	return sum
}

func diagonalSum1(mat [][]int) int {

	sum, n := 0, len(mat[0])

	for i := 0; i < n; i++ {
		sum += mat[i][i] + mat[i][n-1-i]
	}

	if n%2 == 1 {
		sum -= mat[n/2][n/2]
	}

	return sum
}
