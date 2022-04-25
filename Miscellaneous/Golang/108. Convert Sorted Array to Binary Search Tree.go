package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {

	arr := []int{-10, -3, 0, 5, 9}
	result := sortedArrayToBST(arr)
	fmt.Println(result)
}

func sortedArrayToBST(arr []int) *TreeNode {
	n := len(arr)
	if n < 1 {
		return nil
	}

	root := &TreeNode{Val: arr[n/2]}
	root.Left = sortedArrayToBST(arr[:n/2])
	root.Right = sortedArrayToBST(arr[n/2+1:])
	return root
}
