class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def reverseLinklist(self, head):
        curr = head
        prev = None

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev

        return head

obj = Solution()
root = node(1)
root.next = node(2)
root.next = node(3)
ans = obj.reverseLinklist(root)