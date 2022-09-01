class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(root):
    while root is not None:
        print(root.val)
        root = root.next

class Solution:
    def reverseList(self, head):
        if head is None:
            return None

        #Find the middle element of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow

        #Reverse from middle element till end of the list
        prev, curr = None, mid
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        headOfSecond = prev

        #Merge first half and reversed second half of the list
        first, second = head, headOfSecond
        while second.next:
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp

obj = Solution()
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
obj.reverseList(root)
printList(root)