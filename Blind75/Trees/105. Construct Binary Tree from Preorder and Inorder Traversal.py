class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildBinaryTree(preorder, inorder, inStart, inEnd):
    if inStart > inEnd:
        return None

    temp = buildBinaryTree.preIndex
    node = TreeNode(preorder[buildBinaryTree.preIndex])
    buildBinaryTree.preIndex += 1

    if inStart == inEnd:
        return node
    
    inIndex = buildBinaryTree.inOrderMap[preorder[temp]]

    node.left = buildBinaryTree(preorder, inorder, inStart, inIndex - 1)
    node.right = buildBinaryTree(preorder, inorder, inIndex+1, inEnd)

    return node

class Solution:
    def buildTree(self, preorder, inorder):
        buildBinaryTree.preIndex = 0
        buildBinaryTree.inOrderMap = {}

        for i in range(len(inorder)):
            buildBinaryTree.inOrderMap[inorder[i]] = i
                
        return buildBinaryTree(preorder, inorder, 0, len(inorder)-1)
    
    def printTree(self, root):
        if root:
            print(root.val, end=" ")
            self.printTree(root.left)
            self.printTree(root.right)

obj = Solution()
preorder, inorder = [3,9,20,15,7], [9,3,15,20,7]
ans = obj.buildTree(preorder, inorder)
obj.printTree(ans)
print("\n")
