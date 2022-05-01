package main

import "fmt"

func main() {

	nums1, nums2 := []int{1, 2, 2, 1}, []int{2, 2}
	result := intersect(nums1, nums2)
	fmt.Println(result)
}

func intersect(nums1 []int, nums2 []int) []int {
	var ans []int
	tempMap1, tempMap2 := make(map[int]int), make(map[int]int)

	for _, val := range nums1 {
		tempMap1[val]++
	}

	for _, val := range nums2 {
		tempMap2[val]++
	}

	if len(nums1) > len(nums2) {
		for i := 0; i < len(nums1); i++ {
			val, ok := tempMap2[nums1[i]]
			if ok && val > 0 {
				ans = append(ans, nums1[i])
				tempMap2[nums1[i]]--
			}
		}
	} else {
		for i := 0; i < len(nums2); i++ {
			val, ok := tempMap1[nums2[i]]
			if ok && val > 0 {
				ans = append(ans, nums2[i])
				tempMap1[nums2[i]]--
			}
		}
	}

	return ans
}
