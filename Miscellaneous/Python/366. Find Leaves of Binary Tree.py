from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreeLeaves(self, root):
        finalAns = defaultdict(list)

        def getHeight(root):
            if root is None:
                return 0
            
            left = getHeight(root.left)
            right = getHeight(root.right)

            currHeight = max(left, right) + 1
            finalAns[currHeight].append(root.val)
        
            return currHeight
        
        getHeight(root)

        return finalAns.values()

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
obj = Solution()
ans = obj.binaryTreeLeaves(root)
print(ans)
        