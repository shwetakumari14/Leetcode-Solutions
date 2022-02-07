package main

import "fmt"

func main() {

	coordinates := "a1"
	result := squareIsWhite(coordinates)
	fmt.Println(result)
}

func squareIsWhite(coordinates string) bool {
	alphabet, num := int(coordinates[0]-'a'+1), int(coordinates[1])

	if alphabet%2 == 1 && num%2 == 1 {
		return false
	}

	if alphabet%2 == 1 && num%2 == 0 {
		return true
	}

	if alphabet%2 == 0 && num%2 == 0 {
		return false
	}

	if alphabet%2 == 0 && num%2 == 1 {
		return true
	}

	return true
}
