class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeList(self, root1, root2):
        head = tail  = ListNode(0)
        
        while root1 and root2:
            if root1.val < root2.val:
                tail.next = root1
                root1 = root1.next
            else:
                tail.next = root2
                root2 = root2.next
            
            tail = tail.next
        
        tail.next = root1, root2
        
        return head.next

obj = Solution()
root1 = ListNode(1)
root1.next = ListNode(2)
root1.next = ListNode(4)
root2 = ListNode(1)
root2.next = ListNode(3)
root2.next = ListNode(4)
ans = obj.mergeList(root1, root2)
print(ans)