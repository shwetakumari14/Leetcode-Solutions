class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        curr, prev = head, None
        
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        
        return head

obj = Solution()
root = ListNode(1)
root.next = ListNode(2)
root.next = ListNode(3)
ans = obj.reverseList(root)
print(ans)