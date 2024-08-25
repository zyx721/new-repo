class Solution(object):
    def strStr(self, haystack, needle):

        j = 0
        k=0
        if not needle :
            return 0
        for i in range(len(haystack)):
            k=i
            j = 0
            while j<len(needle) and k<len(haystack):
                if haystack[k] == needle[j]:
                    k+=1
                    j+=1
                    if j == len(needle):
                        return i
                else :
                    break
        return -1
s1 = Solution()
print(s1.strStr('lassaddd','sad'))


