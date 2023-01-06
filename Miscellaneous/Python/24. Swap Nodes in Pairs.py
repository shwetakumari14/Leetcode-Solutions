class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):

        curr, nextval, prev, count = head, None, None, 0

        while curr and count < 2:
            nextval = curr.next
            curr.next = prev
            prev = curr
            curr = nextval
            count += 1
        
        if nextval:
            head.next = self.swapPairs(nextval)
        
        return prev
        

obj = Solution()
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = ListNode(6)
ans = obj.swapPairs(node)
while ans:
    print(ans.val, end=" ")
    ans = ans.next
print()