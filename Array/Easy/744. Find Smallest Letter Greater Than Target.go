package main

import "fmt"

func main() {

	letters, target := "cfj", "a"
	lettersByte := []byte(letters)
	targetByte := []byte(target)
	result := nextGreatestLetter(lettersByte, targetByte[0])
	fmt.Println(string(result))
}

func nextGreatestLetter(letters []byte, target byte) byte {
	var ans byte
	for i := 0; i < len(letters); i++ {
		if letters[i] > target {
			ans = letters[i]
			break
		}
	}
	if ans == 0 {
		return letters[0]
	}
	return ans
}
