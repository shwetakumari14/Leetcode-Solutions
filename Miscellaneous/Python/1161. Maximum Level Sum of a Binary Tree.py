import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root):
        maxVal, level, maxLevel = float("-inf"), 0, 0
        q = collections.deque()
        q.append(root)

        while q:
            level += 1
            sumVal = 0

            for _ in range(len(q)):
                node = q.popleft()
                sumVal += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if maxVal < sumVal:
                maxVal, maxLevel = sumVal, level
        
        return maxLevel

root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)

obj = Solution()
ans = obj.maxLevelSum(root)
print(ans)