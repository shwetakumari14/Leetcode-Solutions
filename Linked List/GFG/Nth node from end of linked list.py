class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def getNthFromLast(self, head, n):
        slow, fast, count = head, head, 0
        
        if head:
            while count < n:
                if fast is None:
                    return -1
                fast = fast.next
                count += 1
        
        if fast is None:
            head = head.next
            if head is not None:
                return slow.data
        else:
            
            while fast is not None:
                slow = slow.next
                fast = fast.next
            
            return slow.data

obj = Solution()
root = node(1)
root.next = node(2)
root.next = node(3)
root.next = node(4)
root.next = node(5)
ans = obj.getNthFromLast(root, 2)
print(ans)