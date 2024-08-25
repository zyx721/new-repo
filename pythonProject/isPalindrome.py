class Solution(object):
    def isPalindrome(self, s):
        clean_char = ''.join(char.lower() for char in s if char.isalnum())
        return clean_char == clean_char[::-1]
s =Solution()
print(s.isPalindrome("0P"))