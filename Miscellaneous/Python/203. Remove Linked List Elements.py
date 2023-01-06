class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        temp = ListNode(0)
        temp.next = head

        prev, curr = temp, head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return temp.next
        

obj = Solution()
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(6)
node.next.next.next = ListNode(3)
node.next.next.next.next = ListNode(4)
node.next.next.next.next.next = ListNode(5)
node.next.next.next.next.next.next = ListNode(6)
val = 6
ans = obj.removeElements(node, val)
while ans:
    print(ans.val, end=" ")
    ans = ans.next
print()