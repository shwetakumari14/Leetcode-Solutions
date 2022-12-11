class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthNode(self, head, n):
        temp = ListNode(0)
        temp.next = head

        slow, fast = temp, temp

        for i in range(1, n+2):
            fast = fast.next
        
        while fast is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return temp.next

obj = Solution()
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
ans = obj.removeNthNode(root, 3)
while ans is not None:
    print(ans.val, end=" ")
    ans = ans.next

print()