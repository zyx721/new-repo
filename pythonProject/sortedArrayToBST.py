# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def spd(self,start,end,nums,l=[]):
        if start<end:
            mean = (end - start) // 2
            l.append(nums[mean])
            l += self.spd(start, mean,nums,l)
            l += self.spd(mean, end,nums,l)
        return l
    # def sortedArrayToBST(self, nums):
    #     l = []
    #     start = 0
    #     end = len(nums)-1
    #     while start>end:
    #         mean = (end-start)//2
    #         l.append(nums[mean])
    #         l+=self.spd(start,mean,nums,l)
    #         l+=self.spd(mean,end,nums,l)

nums = [-10,-3,0,5,9]
root1 = TreeNode(0)
root1.left = TreeNode(-3)
root1.right = TreeNode(9)
root1.left.left = TreeNode(-10)

root1.right.left = TreeNode(7)


# Constructing Tr

s =Solution()
print(s.spd(0,len(nums),nums))
