class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def detectLoop(self, head):
        slow, fast = head, head
        
        if head:
            
            while slow is not None and fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                
                if slow == fast:
                    return True
        
        return False

obj = Solution()
root = node(1)
root.next = node(2)
root.next = node(3)
ans = obj.detectLoop(root)
print(ans)