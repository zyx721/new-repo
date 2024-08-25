class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:

            return False
        else:
            print(1)
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def flip_left(self, root):
        if root:
            if not root.left and not root.right:
                return root
            if root.left or root.right:
                k = root.left
                root.left = root.right
                root.right = k
            self.flip_left(root.left)
            self.flip_left(root.right)
        return root

    def isSymmetric(self, root):
        if root:
            if not root.left and not root.right:
                return True
            if not root.left or not root.right:
                return  False
            if root.left:
                root.left = self.flip_left(root.left)
            if root.left and root.right:
                return self.isSameTree(root.left, root.right)
            else:

                return False
        else:

            return True

    def lin(self, root):
        l = []
        if root:
            if root.left:
                l += self.lin(root.left)
            l.append(root.val)
            if root.right:
                l += self.lin(root.right)
            return l
        else:
            return l

    def draw_tree(self, root, depth=0):
        if root is None:
            return
        self.draw_tree(root.right, depth + 1)
        print("   " * depth + str(root.val))
        self.draw_tree(root.left, depth + 1)

# Creating a sample tree
# node = TreeNode(2)
# node.left = TreeNode(3)
# node.right = TreeNode(3)
# node.left.left = TreeNode(4)
# node.left.right = TreeNode(5)
# node.left.right.left = TreeNode(8)
# node.left.right.right = TreeNode(9)
# node.right.left = TreeNode(5)
# node.right.right = TreeNode(4)
# node.right.left.left = TreeNode(9)
# node.right.left.right = TreeNode(8)

node = TreeNode(1)


# Create an instance of the Solution class
s = Solution()
node.left = TreeNode(3)
node.right = TreeNode(3)
# Draw the tree
s.draw_tree(node)
node.left = s.flip_left(node.left)
s.draw_tree(node)
print(s.isSymmetric(node))
