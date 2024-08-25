class Solution(object):
    def rotate(self, matrix):
        nl = []
        for j in range(len(matrix)):
            nl.append([])
        for j in range(len(matrix)):
            for i in range(len(matrix[1])-1,-1,-1):
                nl[j].append(matrix[i][j])

        return nl
s = Solution()
print(s.rotate([[1,2,3],[4,7,9],[6,5,1]]))