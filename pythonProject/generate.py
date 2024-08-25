class Solution(object):
    def generate(self, numRows):
        a = []
        for i in range(numRows):
            if i == 0 or i == 1:
                mn = [1] * (i + 1)
            else:
                mn = [1] * (i + 1)
                for l in range (1,i):
                    mn[l]=a[i-1][l-1]+a[i-1][l]
            a.append(mn)

        return a


s= Solution()
print(s.generate(6))
