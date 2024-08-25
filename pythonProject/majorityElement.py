class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        k=nums[0]
        p=0
        for i in nums:
            if i == k:
                p+=1
            else:
                p=0
            if p > len(nums)/2:
                return i

s = Solution()
print(s.majorityElement([1,1,2,3,1]))
