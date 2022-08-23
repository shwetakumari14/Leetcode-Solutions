class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def linkelistPalindrome(self, head):
        if head is None:
            return True
        
        temp, stack = head, []

        while temp is not None:
            stack.append(temp.data)
            temp = temp.next
        
        while head is not None:
            if stack.pop() != head.data:
                return False
            head = head.next
        
        return True

obj = Solution()
root = node(1)
root.next = node(2)
root.next = node(1)
ans = obj.linkelistPalindrome(root)
print(ans)