class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkRange(data, low, high):
    if data >= low and data <= high:
        return True
    
    return False

class Solution:
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0
        stack, ans = [root], 0

        while stack:
            node = stack.pop()
            if checkRange(node.val, low, high):
                ans += node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return ans

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right = TreeNode(15)
root.right.right = TreeNode(18)
obj = Solution()
low, high = 7, 15
ans = obj.rangeSumBST(root, low, high)
print(ans)