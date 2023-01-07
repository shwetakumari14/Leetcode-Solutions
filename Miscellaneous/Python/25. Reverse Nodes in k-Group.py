class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head, k):
        nextHead, ptr = None, head

        while k:
            nextval = ptr.next
            ptr.next= nextHead
            nextHead = ptr
            ptr = nextval
            k -= 1
        
        return nextHead

    def reverseKGroup(self, head, k):
        count, ptr = 0, head

        while ptr and count < k:
            ptr = ptr.next
            count += 1
        
        if count == k:
            reversedHead = self.reverse(head, k)
            head.next = self.reverseKGroup(ptr, k)

            return reversedHead
        
        return head
        

obj = Solution()
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
ans = obj.reverseKGroup(node, 3)
while ans:
    print(ans.val, end=" ")
    ans = ans.next
print()