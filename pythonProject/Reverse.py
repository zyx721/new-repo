class Solution(object):
    def reverse(self, x):
        if x > 0:
            s = 0
            while x != 0:
                d = x % 10
                s = s * 10 + d
                x = x // 10
            if  s > 2 ** 31 - 1:
                return 0
            return s
        else:
            x = x * -1
            s = 0
            while x != 0:
                d = x % 10
                s = s * 10 + d
                x = x // 10
            if s < -2 ** 31 :
                return 0
            return -1 * s
