class Solution(object):
    def plusOne(self, digits):
        digits[len(digits)-1] +=1
        k = len(digits)-1
        while digits[k] == 10 :
            if k == 0 :
                digits.append(0)
                digits[0] =1
                break
            digits[k-1] += 1
            digits[k] = 0
            k = k-1

        return digits


a=[9]
s = Solution()
a = s.plusOne(a)
print(a)