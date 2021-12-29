package main

import "fmt"

func main() {

	candies := []int{2, 3, 5, 1, 3}
	extraCandies := 3
	result := kidsWithCandies(candies, extraCandies)
	fmt.Println(result)
}

func kidsWithCandies(candies []int, extraCandies int) []bool {
	maxCandies := 0
	for _, eachCandy := range candies {
		if maxCandies < eachCandy {
			maxCandies = eachCandy
		}
	}

	var ans []bool
	for _, eachCandy := range candies {
		if eachCandy+extraCandies >= maxCandies {
			ans = append(ans, true)
		} else {
			ans = append(ans, false)
		}
	}

	return ans

}
