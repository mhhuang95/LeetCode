class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        ls = len(height)
        i = 0
        while i < ls-1:
            temp = -1
            for j in range(i+1, ls):
                if height[j] > height[i]:
                    k = j
                    break
                if height[j] <= height[i] and height[j] >= temp:
                    temp = height[j]
                    k = j
            res = res + self.calculateArea(height[i:k+1])
            i = k
        return res

    def calculateArea(self, h):
        ls = len(h)
        hei = min(h[0], h[-1])
        area = 0
        for i in range(1,ls-1):
            area = area + max(0, hei - h[i])
        return area

if __name__ == "__main__":
    s = Solution()
    print(s.trap([2,0,2]))