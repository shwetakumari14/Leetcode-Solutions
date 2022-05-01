class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, head, num):
        traveser = head

        while traveser is not None:
            if traveser.next.val == num:
                traveser.next = traveser.next.next
                return head
            else:
                traveser = traveser.next
       
        
        return head
        
obj = Solution()
list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)
ans = obj.deleteNode(list, 3)
while ans is not None:
    print(ans.val)
    ans = ans.next