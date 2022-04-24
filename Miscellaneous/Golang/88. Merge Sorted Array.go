package main

import "fmt"

func main() {

	nums1, m, nums2, n := []int{1, 2, 3, 0, 0, 0}, 3, []int{2, 5, 6}, 3
	result := mergeSortedArray(nums1, nums2, m, n)
	fmt.Println(result)
}

func mergeSortedArray(nums1, nums2 []int, m, n int) []int {

	for n > 0 {
		if m > 0 && nums1[m-1] >= nums2[n-1] {
			nums1[m+n-1] = nums1[m-1]
			m -= 1
		} else {
			nums1[m+n-1] = nums2[n-1]
			n -= 1
		}
	}

	return nums1
}
