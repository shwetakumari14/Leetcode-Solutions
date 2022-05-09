package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {

	root := &TreeNode{4, nil, nil}
	root.Left = &TreeNode{2, nil, nil}
	root.Left.Left = &TreeNode{1, nil, nil}
	root.Left.Right = &TreeNode{4, nil, nil}
	root.Right = &TreeNode{7, nil, nil}
	root.Right.Left = &TreeNode{6, nil, nil}
	root.Right.Right = &TreeNode{9, nil, nil}
	result := invertTree(root)
	fmt.Println(result)

}

func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	invertTree(root.Left)
	invertTree(root.Right)

	var temp *TreeNode
	temp = root.Left
	root.Left = root.Right
	root.Right = temp

	return root

}
