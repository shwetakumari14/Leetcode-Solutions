class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head):
        slow, fast = head, head
        
        if head is not None:
            while slow and fast and fast.next:
                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    return "Cycle Detected"
        
        return "Cycle Not Detected"