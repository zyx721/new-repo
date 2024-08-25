class Solution(object):
    def myAtoi(self, s):
        niggative = 1
        k=0
        found_digit = False
        for a in range(len(s)):
            if s[a] == ' ':
                if found_digit:
                    break
                continue
            elif s[a] == '-' or s[a]=='+':
                if found_digit:
                    break
                niggative = -1 if s[a] == '-' else 1
                found_digit = True
            elif s[a].isdigit():
                found_digit = True
                k = k*10 + int(s[a])
            else:
                break



        k  *= niggative
        k = max(min(k, 2 ** 31 - 1), -2 ** 31)

        return k


s = Solution()
print(s.myAtoi('    +12340 qwqq'))
