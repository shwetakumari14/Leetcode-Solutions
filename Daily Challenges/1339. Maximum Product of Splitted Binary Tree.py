class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root):
        if not root:
            return 0
        
        subTreeOneSum = []
        
        def treeSum(node):
            if not node:
                return 0
            
            left = treeSum(node.left)
            right = treeSum(node.right)
            subTreeSum = node.val + left + right
            subTreeOneSum.append(subTreeSum)

            return subTreeSum
        
        totalTreeSum, maxProd = treeSum(root), 0

        for subTreeOne in subTreeOneSum:
            subTreeTwo = totalTreeSum - subTreeOne
            product = subTreeOne * subTreeTwo
            maxProd = max(maxProd, product)
        
        return maxProd % (10 ** 9 + 7)

    


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
obj = Solution()
ans = obj.maxProduct(root)
print(ans)