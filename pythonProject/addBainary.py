class Solution(object):
    def addBinary(self, a, b):
        A = [int(digit) for digit in str(a)]
        B = [int(digit) for digit in str(b)]
        print(B)
        print(A)
        if len(A)<len(B):
            A.reverse()
            while len(B) > len(A):
                A.append(0)
            A.reverse()
        if len(A)>len(B):
            B.reverse()
            while len(B) < len(A):
                B.append(0)
            B.reverse()
        print(B)
        print(A)
        S =[]
        for i in range(len(A)):
            w = len(A)-i-1
            if A[w]+ B[w] == 1 or  A[w]+ B[w] == 0:
                S.append(A[w] + B[w])
                print(S)
            else:
                if w == 0 and A[w]+ B[w] ==2 :
                    S.append(0)
                    S.append(1)
                    break
                if A[w]+ B[w] == 2 :
                    S.append(0)
                    A[w-1]+=1
                if w == 0 and A[w]+ B[w] ==3 :
                    S.append(1)
                    S.append(1)
                    break
                if A[w]+ B[w] ==3:
                    S.append(1)
                    A[w - 1] += 1
        S.reverse()
        SS=''
        for k in range(len(S)):
            SS+=str(S[k])

        return SS







s = Solution()
print(s.addBinary("11","1"))

