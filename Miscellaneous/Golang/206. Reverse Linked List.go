package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {

	list := &ListNode{1, nil}
	list.Next = &ListNode{2, nil}
	list.Next.Next = &ListNode{3, nil}
	list.Next.Next.Next = &ListNode{4, nil}
	result := reverseList(list)

	for result != nil {
		fmt.Print(result.Val, " ")
		result = result.Next
	}

}

func reverseList(head *ListNode) *ListNode {
	curr := head
	var prev *ListNode

	for curr != nil {
		next := curr.Next
		curr.Next = prev
		prev = curr
		curr = next
	}
	head = prev

	return head
}
