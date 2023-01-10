import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        
        columnTable = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node:
                columnTable[column].append(node.val)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
        
        
        return [columnTable[i] for i in sorted(columnTable.keys())]


obj = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
ans = obj.verticalOrder(root)
print(ans)