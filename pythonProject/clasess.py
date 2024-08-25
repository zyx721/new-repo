class Solution(object):
    def maxArea(self, height):
        maxarea = 0
        for i in range(len(height) ):
            for j in range(i,len(height)):
                M = (j - i) * min(height[i], height[j])
                maxarea = max(maxarea,M)
        return maxarea


s1 = Solution()
h = [2,3,4,5,18,17,6]
print(s1.maxArea(h))