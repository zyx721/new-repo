class Solution(object):
    def removeElement(self, nums, val):
        i=0
        for j in range (0,len(nums)):
            if(nums[j] != val):
                nums[i]=nums[j]
                i+=1
        return i










nums =[1,2,3,3,3,5,6]
s = Solution()
num = s.removeElement(nums,3)
print(num)
for k in range (0,num):
    print(nums[k],end=' ')