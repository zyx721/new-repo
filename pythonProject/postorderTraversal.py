# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        num = []
        if root:
            num.append(root.val)
            if root.left:
                num.extend(self.postorderTraversal(root.left))
            if root.right:
                num.extend(self.postorderTraversal(root.right))
        return num


s=Solution()

root1 = TreeNode(0)
root1.left = TreeNode(-3)
root1.right = TreeNode(9)
root1.left.left = TreeNode(-10)

root1.right.left = TreeNode(7)
print(s.postorderTraversal(root1))