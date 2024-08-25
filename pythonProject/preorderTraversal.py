# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        l = []
        if root:
            l.append(root.val)
            if root.left:
                l += self.preorderTraversal(root.left)
            if root.right:
                l += self.preorderTraversal(root.right)
            return l
        else:
            return
