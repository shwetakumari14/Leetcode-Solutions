class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        stack = []
        temp = head
        
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        
        while head is not None:
            val = stack.pop()
            if head.val is not val:
                return False
            head = head.next
       
        
        return True
        
obj = Solution()
list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(2)
list.next.next.next = ListNode(1)
ans = obj.isPalindrome(list)
print(ans)