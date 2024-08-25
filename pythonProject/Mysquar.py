class Solution(object):
    def mySqrt(self, x):
        y=x//2
        if x == 1:
            return 1
        while y*y > x:
            y=y//2
        while y*y<x:
            y+=1
        if y*y == x:
            return y
        return y-1

s =Solution()
print(s.mySqrt(9))
