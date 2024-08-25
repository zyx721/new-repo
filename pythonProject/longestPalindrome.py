class Solution(object):
    def ispalindrome(self,s):
        return s == s[::-1]
    def longestPalindrome(self, s):
        n=""
        l=0
        for i in range(len(s)):
            k = ""
            for j in range(i,len(s)):
                k+=s[j]
                if self.ispalindrome(k):
                    if len(k)>l:
                        l=len(k)
                        n=k
        return n



s =Solution()
print(s.longestPalindrome("a"))