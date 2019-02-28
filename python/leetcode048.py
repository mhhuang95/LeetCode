class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        ls = len(matrix)
        for i in range((ls-1)//2+1):
            for j in range(ls//2):
                print(i,j)
                temp = matrix[i][j]
                matrix[i][j] = matrix[ls-1-j][ i]
                matrix[ls-1-j][i] = matrix[ls-1-i][ls-1-j]
                matrix[ls - 1 - i][ls - 1 - j] = matrix[j][ls-1-i]
                matrix[j][ls - 1 - i] = temp
        print(matrix)
        return

if __name__ == '__main__':
    # begin
    s = Solution()
    s.rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])






