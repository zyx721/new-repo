# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        l = []
        if root:

            if root.left:
                l += self.inorderTraversal(root.left)
            l.append(root.val)
            if root.right:
                l+=self.inorderTraversal(root.right)
                print(l)
            return l
        else:
            return l

node = TreeNode(3)
node.left = TreeNode(1)
node.right = TreeNode(5)
node.left.left = TreeNode(0)
node.left.right = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(6)
s =Solution()
print(s.inorderTraversal(node))