package main

import "fmt"

func main() {

	nums1, nums2, nums3 := []int{3, 1}, []int{2, 3}, []int{1, 2}
	result := twoOutOfThree(nums1, nums2, nums3)
	fmt.Println(result)
}

func twoOutOfThree(nums1 []int, nums2 []int, nums3 []int) []int {
	map1, map2, map3, anMap := make(map[int]int), make(map[int]int), make(map[int]int), make(map[int]int)

	for _, val := range nums1 {
		map1[val]++
	}

	for _, val := range nums2 {
		map2[val]++
	}

	for _, val := range nums3 {
		map3[val]++
	}

	for key, val := range map1 {
		count, ok := map2[key]
		if ok && count > 0 && val > 0 {
			anMap[key]++
			map1[key]--
			map2[key]--
		}
	}

	for key, val := range map2 {
		count, ok := map3[key]
		if ok && count > 0 && val > 0 {
			anMap[key]++
			map2[key]--
			map3[key]--
		}
	}

	for key, val := range map3 {
		count, ok := map1[key]
		if ok && count > 0 && val > 0 {
			anMap[key]++
			map3[key]--
			map1[key]--
		}
	}

	var ans []int

	for key := range anMap {
		ans = append(ans, key)
	}

	return ans
}
