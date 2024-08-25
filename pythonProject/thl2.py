class Solution(object):
    def myPow(self, x, n):
        p = 1
        if n > 0:
            p = x**n
        else:
            p =  x**n
        return p
s = Solution()
print(s.myPow(2,3))
