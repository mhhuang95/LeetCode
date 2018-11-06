class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        ls = len(matrix)
        if ls == 1:
            return self.binary(matrix[0], target)
        i = 0
        if matrix[i][0] > target:
            return False
        while i < ls:
            if matrix[i][0] > target:
                break
            i += 1
        row = i-1
        return self.binary(matrix[row], target)


    def binary(self,l, target):
        ls= len(l)
        start = 0
        end = ls-1
        while end >= start:
            mid = (start+end)//2
            if l[mid] == target:
                return True
            elif l[mid] < target:
                start = mid+1
            else:
                end = mid - 1
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix([[1],[3]],1))