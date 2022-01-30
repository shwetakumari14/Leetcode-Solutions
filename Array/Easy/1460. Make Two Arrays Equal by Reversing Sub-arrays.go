package main

import (
	"fmt"
	"sort"
)

func main() {

	target, arr := []int{1, 2, 3, 4}, []int{2, 4, 1, 3}
	result := canBeEqual3(target, arr)
	fmt.Println(result)
}

func canBeEqual(target []int, arr []int) bool {

	sort.Ints(target)
	sort.Ints(arr)

	if len(target) != len(arr) {
		return false
	} else {
		for i := 0; i < len(target); i++ {
			if target[i] != arr[i] {
				return false
			}
		}
	}

	return true

}

func canBeEqual2(target []int, arr []int) bool {

	map1, map2 := make(map[int]int), make(map[int]int)

	if len(target) != len(arr) {
		return false
	} else {
		for _, val := range target {
			map1[val]++
		}

		for _, val := range arr {
			map2[val]++
		}

		for key, val := range map1 {
			count, ok := map2[key]
			if !ok || val != count {
				return false
			}
		}
	}

	return true

}

func canBeEqual3(target []int, arr []int) bool {

	map1 := make(map[int]int)

	if len(target) != len(arr) {
		return false
	} else {
		for i := 0; i < len(target); i++ {
			map1[arr[i]]++
			map1[target[i]]--
		}

		for _, val := range map1 {
			if val != 0 {
				return false
			}
		}
	}

	return true

}
