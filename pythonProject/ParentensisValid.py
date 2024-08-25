class Solution(object):
    def Parentensisvalid(self,s):
        stack =[]
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack or (i == ')' and stack[-1] != '(')\
                    or (i == '}' and stack[-1] != '{')\
                    or (i == ']' and stack[-1] != '[') :
                    return False
                stack.pop()
        return not stack
s1 = Solution()
print(s1.Parentensisvalid(''))


