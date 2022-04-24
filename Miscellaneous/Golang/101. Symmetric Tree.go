package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {

	root := &TreeNode{1, nil, nil}
	root.Left = &TreeNode{2, nil, nil}
	root.Left.Left = &TreeNode{3, nil, nil}
	root.Left.Right = &TreeNode{4, nil, nil}
	root.Right = &TreeNode{2, nil, nil}
	root.Right.Left = &TreeNode{4, nil, nil}
	root.Right.Right = &TreeNode{3, nil, nil}
	result := isSymmetric(root)
	fmt.Println(result)
}

func isSymmetric(root *TreeNode) bool {

	return isMirror(root, root)
}

func isMirror(root1, root2 *TreeNode) bool {
	if root1 == nil && root2 == nil {
		return true
	}

	if root1 != nil && root2 != nil {
		if root1.Val == root2.Val {
			return (isMirror(root1.Left, root2.Right)) && (isMirror(root1.Right, root2.Left))
		}
	}

	return false
}
