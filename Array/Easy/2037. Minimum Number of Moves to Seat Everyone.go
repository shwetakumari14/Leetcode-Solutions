package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {

	seats, students := []int{3, 1, 5}, []int{2, 7, 4}
	result := minMovesToSeat(seats, students)
	fmt.Println(result)
}

func minMovesToSeat(seats []int, students []int) int {

	ans := 0
	sort.Ints(seats)
	sort.Ints(students)

	for i := 0; i < len(seats); i++ {
		ans += int(math.Abs(float64(students[i] - seats[i])))
	}

	return ans
}
