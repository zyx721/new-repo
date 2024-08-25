class Solution(object):
    def merge(self, nums1, m, nums2, n):
        l = m-1
        r = n-1
        i = m+n-1

        while l>=0 and r>=0 :
            if nums1[l]<nums2[r]:
                nums1[i]=nums2[r]
                i-=1
                r-=1
            else:
                nums1[i]=nums1[l]
                l-=1
                i-=1
        if r>=0 :
            for k in range(0,i+1):
                nums1[k] = nums2[k]


        return nums1

s = Solution()
print(s.merge([4,0,0,0,0,0],1,[5,6,7,],3))
