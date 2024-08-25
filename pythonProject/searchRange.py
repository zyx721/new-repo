class Solution(object):
    def searchRange(self, nums, target):
        l=0
        r=len(nums)
        if r == 0 :
            return [-1,-1]
        k= (l+r)//2

        while r >= l:
            if r-l == 1:
                k = 0
            if nums[k] == target:
                p = k-1
                c = []
                while nums[k] == target and k < len(nums):
                    c.append(k)
                    k+=1
                    if k == len(nums):
                        break
                while nums[p] == target and p > 0:
                    c.append(p)
                    k-=1
                    if p == 0:
                        break
                return [c[0] ,c [len(c)-1]]
            if nums[k] > target:
                r = k
            else:
                if nums[k]< target:
                    l = k
            k = (l + r) // 2
            if k ==0 or k == l or target<nums[0] or nums[len(nums)-1]<target :
                return [-1,-1]

        return [-1,-1]
sol = Solution()
print(sol.searchRange([1,2,3], 1))  # Output should be [0, 0]
print(sol.searchRange([5,7,7,8,8,10], 8))  # Output should be [3, 4]
print(sol.searchRange([5,7,7,8,8,10], 6))  # Output should be [-1, -1]
