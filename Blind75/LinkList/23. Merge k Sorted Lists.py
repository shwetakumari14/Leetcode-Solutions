class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, left, right):
        if not left or not right:
            return left or right
        
        if left.val < right.val:
            left.next = self.merge(left.next, right)
            return left
        
        right.next = self.merge(left, right.next)
        return right


    def mergeKLists(self, lists):
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge(left, right)

obj = Solution()
lists = [[1,4,5],[1,3,4],[2,6]]
ans = obj.mergeKLists(lists)
print(ans)