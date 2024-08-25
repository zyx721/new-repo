class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s)-1
        n=0
        while s[i] == ' ':
            i-=1
        while i >= 0 and s[i] != ' ' :
            i-=1
            n+=1
        return n
s1 = Solution()
print(s1.lengthOfLastWord("salam 3likm ziad  "))


