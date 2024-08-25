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
    def isBalanced(self, root):
        if not root:
            return True
        l= self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        if l-r > 1 or l-r<-1:
            return False

        return self.isBalanced(root.right)and self.isBalanced(root.left)



s = Solution()
root1 = TreeNode(0)
root1.left = TreeNode(-3)
root1.right = TreeNode(9)


root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(7)

print(s.isBalanced(root1))