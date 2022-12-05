class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        slow, fast = head, head

        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow.val

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
obj = Solution()
ans = obj.middleNode(root)
print(ans)