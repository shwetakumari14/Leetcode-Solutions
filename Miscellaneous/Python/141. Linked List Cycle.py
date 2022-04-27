class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        slow, fast = head, head

        if head is not None:
            while slow is not None and fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    return True

        return False