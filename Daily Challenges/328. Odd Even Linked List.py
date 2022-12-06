class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if not head:
            return None
        
        odd, even = head, head.next
        evenHead = even

        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenHead

        return head
                    
list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)
list.next.next.next.next = ListNode(5)

obj = Solution()
ans = obj.oddEvenList(list)
while ans is not None:
    print(ans.val, end=" ")
    ans = ans.next
print()