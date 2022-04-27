package main

import (
	"fmt"
)

type MinStack struct {
	Stack [][]int
}

func Constructor() MinStack {
	return MinStack{}
}

func (this *MinStack) Push(val int) {
	currMin := this.GetMin()
	if currMin == 0 || val < currMin {
		currMin = val
	}
	temp := make([]int, 2)
	temp[0], temp[1] = val, currMin
	this.Stack = append(this.Stack, temp)
}

func (this *MinStack) Pop() {
	this.Stack = this.Stack[:len(this.Stack)-1]
}

func (this *MinStack) Top() int {
	if len(this.Stack) == 0 {
		return 0
	}
	return this.Stack[len(this.Stack)-1][0]
}

func (this *MinStack) GetMin() int {
	if len(this.Stack) == 0 {
		return 0
	}
	return this.Stack[len(this.Stack)-1][1]
}

func main() {
	obj := Constructor()
	obj.Push(10)
	obj.Push(5)
	obj.Pop()
	obj.Push(2)
	obj.Push(12)
	param_3 := obj.Top()
	param_4 := obj.GetMin()
	fmt.Println(param_3, " ", param_4)
}
