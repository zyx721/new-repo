class Solution(object):
    def singleNumber(self, nums):
        l = []
        for i in nums:
            if i in l:
                l.remove(i)
            else:
                l.append(i)
        return l[0]

