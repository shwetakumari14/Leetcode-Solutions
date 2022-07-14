class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def removeDuplicates(self, head):
        temp = head
        
        if temp is None:
            return None
        
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        
        return head

obj = Solution()
root = node(1)
root.next = node(2)
root.next = node(3)
root.next = node(3)
root.next = node(5)
ans = obj.removeDuplicates(root)
print(ans)