package main

import "fmt"

func main() {

	image := [][]int{{1, 1, 0}, {1, 0, 1}, {0, 0, 0}}
	result := flipAndInvertImage(image)
	fmt.Println(result)

}

func flipAndInvertImage(image [][]int) [][]int {

	var ans [][]int

	for _, img := range image {
		flipImage(img)
		invertImage(img)
		ans = append(ans, img)
	}

	return ans
}

func flipImage(arr []int) []int {

	for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
		arr[i], arr[j] = arr[j], arr[i]
	}

	return arr
}

func invertImage(arr []int) []int {

	for i := 0; i < len(arr); i++ {
		if arr[i] == 0 {
			arr[i] = 1
		} else if arr[i] == 1 {
			arr[i] = 0
		}
	}

	return arr
}
