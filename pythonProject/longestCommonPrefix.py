class Solution(object):
    def longestCommonPrefix(self, strs):
        list=[]
        l = min(len(s) for s in strs)
        i=0
        prefix = ''
        while i<l :
            v = strs[0][i]
            if all(v == strs[s][i] for s in strs):
                prefix += strs[0][i]
                i+=1
            else:
                return prefix
        return prefix


