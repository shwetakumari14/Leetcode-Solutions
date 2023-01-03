from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return None
        
        level_queue = deque()
        result, is_left_node = [], True
        node_queue = deque([root, None])

        while node_queue:
            curr_node = node_queue.popleft()

            if curr_node:
                if is_left_node:
                    level_queue.append(curr_node.val)
                else:
                    level_queue.append(curr_node.val)
                
                if curr_node.left:
                    node_queue.append(curr_node.left)
                
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                result.append(level_queue)
                if len(node_queue) > 0:
                    node_queue.append(None)
                
                level_queue = deque()
                is_left_node = not is_left_node
        
        return result


obj = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
ans = obj.zigzagLevelOrder(root)
print(ans)