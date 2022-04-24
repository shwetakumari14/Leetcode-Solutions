package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {

	root := &TreeNode{1, nil, nil}
	root.Right = &TreeNode{2, nil, nil}
	root.Right.Left = &TreeNode{3, nil, nil}
	result := inorderTraversal(root)
	fmt.Println(result)

}

func inorderTraversal(root *TreeNode) []int {
	if root == nil {
		return nil
	}

	var ans []int
	ans = append(ans, inorderTraversal(root.Left)...)
	ans = append(ans, root.Val)
	ans = append(ans, inorderTraversal(root.Right)...)

	return ans
}
