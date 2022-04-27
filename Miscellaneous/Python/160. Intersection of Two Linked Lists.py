class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):

        if headA is None or headB is None:
            return None

        curA = headA
        curB = headB

        while curA is not curB:
            curA = headB if curA is None else curA.next
            curB = headA if curB is None else curB.next

        return curA