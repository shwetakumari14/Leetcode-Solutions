class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBSTUntil(root, mini, maxi):
    if root is None:
        return True
    
    if root.val < mini or root.val > maxi:
        return False

    return isBSTUntil(root.left, mini, root.val-1) and isBSTUntil(root.right, root.val+1, maxi)

class Solution:
    def isValidBST(self, root):
       return isBSTUntil(root, float("-inf"), float("inf")) 
       

obj = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
ans = obj.isValidBST(root)
print(ans)
