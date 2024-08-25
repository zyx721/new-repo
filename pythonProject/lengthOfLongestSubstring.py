class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i=0
        n=0
        while i != len(s):
            if s[i] != s[i+1]:
                n+=1
                
            i+=1
        print(n)
        return n
s1 = Solution()
s = "bbbbb"
s1.lengthOfLongestSubstring(s)