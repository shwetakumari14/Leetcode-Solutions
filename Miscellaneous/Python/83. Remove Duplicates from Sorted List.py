class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, root):
        if root is None:
            return None
        
        curr = root

        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return node


obj = Solution()
node = ListNode(1)
node.next = ListNode(1)
node.next.next = ListNode(2)
node.next.next.next = ListNode(3)
node.next.next.next.next = ListNode(3)
ans = obj.deleteDuplicates(node)
while ans is not None:
    print(ans.val, end=" ")
    ans = ans.next
print()