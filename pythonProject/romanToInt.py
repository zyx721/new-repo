class Solution(object):
    def romanToInt(self, s):
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans=0
        for ss in range (len(s)):
            ans += m[s[ss]]
            if len(s)-1>ss and  m[s[ss]]<m[s[ss+1]]:
                ans = ans -2*m[s[ss]]
        return ans

s = Solution()
print(s.romanToInt("MCMXCIV"))
