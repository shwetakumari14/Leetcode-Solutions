class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(head, data):
    if head is None:
        return None
    
    temp = head

    while temp is not None and temp.next is not None:
        if temp.next.val == data:
            temp.next = temp.next.next
            return head
        else:
            temp = temp.next

class Solution:
    def removeNthNode(self, head, n):
        slow, fast, count = head, head, 0

        if head:
            while count < n:
                if fast is None:
                    return None
                fast = fast.next
                count += 1
            
            if fast is None:
                head = head.next
                if head is not None:
                    deleteNode(head, slow.val)
            else:
                while fast is not None:
                    slow = slow.next
                    fast = fast.next

                deleteNode(head, slow.val)

        return head

obj = Solution()
root = ListNode(1)
root.next = ListNode(2)
root.next = ListNode(3)
root.next = ListNode(4)
root.next = ListNode(5)
ans = obj.removeNthNode(root, 3)
print(ans)