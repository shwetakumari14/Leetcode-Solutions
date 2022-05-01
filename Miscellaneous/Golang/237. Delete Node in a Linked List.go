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
	result := isPalindrome(list, 3)

	for result != nil {
		fmt.Println(result.Val)
		result = result.Next
	}
}

func isPalindrome(head *ListNode, num int) *ListNode {
	temp := head

	for temp != nil {
		if temp.Next.Val == num {
			temp.Next = temp.Next.Next
			return head
		} else {
			temp = temp.Next
		}
	}

	return head
}
