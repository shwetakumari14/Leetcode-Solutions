from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):

        def buildBinaryTree(left, right):
            if left > right:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)

            index = inorder_map[val]

            root.right = buildBinaryTree(index+1, right)
            root.left = buildBinaryTree(left, index - 1)

            return root
        

        inorder_map = {val:idx for idx, val in enumerate(inorder)}
        return buildBinaryTree(0, len(inorder)-1)

obj = Solution()
inorder, postorder = [9,3,15,20,7], [9,15,7,20,3]
ans = obj.buildTree(inorder, postorder)
print(ans)