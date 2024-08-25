class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s:
            ret = [0]*len(s)
            re = 0
            l = []
            for sq in range(len(s)):
                if s[sq] in l:
                    re += 1
                    f = 1
                    l = []
                    k = 0
                    l.append(s[sq])
                    for i in range(1,sq):
                        if s[(sq - i)] != s[sq] and s[(sq - i)] not in l :
                            l.append(s[sq - i])
                            f+=1
                        else:

                            break

                    ret[re]+=f
                else:
                    ret[re] += 1
                    l.append(s[sq])

            return max(ret)
        else:
            return 0

s =Solution()
print(s.lengthOfLongestSubstring("aab"))
