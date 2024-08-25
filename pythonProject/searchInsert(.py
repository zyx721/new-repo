class Solution(object):
    def searchInsert(self, nums, target):
        i=0
        while i<len(nums) and nums[i]<=target:
            if nums[i] == target:
                return i
            i+=1
            print(i)
        return i
s = Solution()
print(s.searchInsert([1,3,4,5,6],9))