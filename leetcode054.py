class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if len(matrix)==0:
            return res
        length = len(matrix)*len(matrix[0])
        i = 0
        j = 0
        m = 0
        n = 0
        res.append(matrix[m][n])
        matrix[m][n] = None
        i = i + 1
        while i < length:
            if j%4 == 0:

                while n+1 < len(matrix[0]) and matrix[m][n+1] !=None :
                    n = n+1
                    res.append(matrix[m][n])
                    matrix[m][n] = None
                    i=i+1
                j=j+1
            if j%4 == 1:

                while m+1 < len(matrix) and matrix[m+1][n] !=None:
                    m = m + 1
                    res.append(matrix[m][n])
                    matrix[m][n] = None
                    i=i+1
                j=j+1
            if j % 4 == 2:

                while n - 1 >=0 and matrix[m][n -1] != None:
                    n = n - 1
                    res.append(matrix[m][n])
                    matrix[m][n] = None
                    i = i + 1
                j = j + 1
            if j % 4 == 3:

                while m - 1 >=0 and matrix[m - 1][n] != None :
                    m = m - 1
                    res.append(matrix[m][n])
                    matrix[m][n] = None
                    i = i + 1
                j = j + 1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]))