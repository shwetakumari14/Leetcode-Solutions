class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def isPalindrome(self, head):
        temp, data = head, []
        
        while temp:
            data.append(temp.data)
            temp = temp.next
        
        while head:
            if data.pop() != head.data:
                return 0
            head = head.next
        
        return 1

obj = Solution()
root = node(1)
root.next = node(2)
root.next = node(1)
ans = obj.isPalindrome(root)
print(ans)