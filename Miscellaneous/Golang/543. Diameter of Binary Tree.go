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
	root.Left.Left = &TreeNode{4, nil, nil}
	root.Left.Right = &TreeNode{5, nil, nil}
	root.Right = &TreeNode{3, nil, nil}
	result := diameterOfTree(root)
	fmt.Println(result)

}

func height(root *TreeNode) int {
	if root == nil {
		return 0
	}

	return 1 + max(height(root.Left), height(root.Right))
}

func diameterOfTree(root *TreeNode) int {
	if root == nil {
		return 0
	}

	lheight := height(root.Left)
	rheight := height(root.Right)

	ldiameter := diameterOfTree(root.Left)
	rdiameter := diameterOfTree(root.Right)

	return max(lheight+rheight, max(ldiameter, rdiameter))

}

func max(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
