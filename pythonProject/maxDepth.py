# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        cntr = 0
        r = 0
        l = 0
        if root:
            cntr+=1
            if root.left:
                r= self.maxDepth(root.left)
            if root.right:
                l=self.maxDepth(root.right)
        cntr +=max(r,l)
        return cntr

node = TreeNode(2)
node.left = TreeNode(3)

node.left.left = TreeNode(4)



s = Solution()
print(s.maxDepth(node))