package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {

	list := &ListNode{1, nil}
	list.Next = &ListNode{2, nil}
	list.Next.Next = &ListNode{2, nil}
	list.Next.Next.Next = &ListNode{1, nil}
	result := isPalindrome(list)
	fmt.Println(result)
}

func isPalindrome(head *ListNode) bool {
	temp := head
	var stack []int

	for temp != nil {
		stack = append(stack, temp.Val)
		temp = temp.Next
	}

	for head != nil {
		val := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if val != head.Val {
			return false
		}
		head = head.Next
	}

	return true
}
