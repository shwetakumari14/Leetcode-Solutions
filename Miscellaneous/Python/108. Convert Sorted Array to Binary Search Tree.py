class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, arr):
        n = len(arr)
        if n < 1:
            return None
        
        idx = (n-1)//2

        root = TreeNode(arr[idx])
        root.left = self.sortedArrayToBST(arr[:idx])
        root.right = self.sortedArrayToBST(arr[idx+1:])

        return root
    

obj = Solution()
arr = [-10,-3,0,5,9]
ans = obj.sortedArrayToBST(arr)
print(ans)