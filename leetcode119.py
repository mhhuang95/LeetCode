class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        tria = [1]
        for i in range(rowIndex-1):
            x = [1]
            for j in range(len(tria)-1):
                x.append(tria[j]+tria[j+1])
            x.append(1)
            tria = x
        return tria

    
if __name__ == "__main__":
    s = Solution()
    print(s.getRow(3))
