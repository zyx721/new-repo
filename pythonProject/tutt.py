class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i =0
        for j in range(1,len(nums)) :
            if(nums[i] != nums[j]):
                i=i+1
                nums[i]=nums[j]

        return i+1


nums = [1,1,2,2,3,4,5]
sol1 = Solution()
s = sol1.removeDuplicates(nums)
print(s)
for i in range(0,s):
    print(nums[i],end=' ')