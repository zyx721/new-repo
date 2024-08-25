class Solution(object):
    def divide(self, dividend, divisor):

        if divisor>0 and dividend>0 or (divisor<0 and dividend<0) :
            if (divisor<0 and dividend<0):
                divisor*=-1
                dividend*=-1
            num = 0
            f=0
            while num<dividend and num+divisor<=dividend:
                num+=divisor
                f+=1
        else :
            if divisor<0:
                divisor*=-1
            if dividend < 0:
                dividend *= -1

            num = 0
            f = 0
            while num < dividend and num + divisor <= dividend:
                num += divisor
                f += 1
            f*=-1
        return f
s = Solution()
print(s.divide(1,1))