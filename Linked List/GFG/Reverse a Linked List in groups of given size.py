class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def reverse(self,head, k):
        # Code here
        curr, prev, next, count = head, None, None, 0
        if head is None:
            return None
        
        while curr is not None and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
        
        if next is not None:
            head.next = self.reverse(next, k)
        
        return prev

obj = Solution()
root = node(1)
root.next = node(2)
root.next = node(3)
ans = obj.reverse(root, 2)
print(ans)