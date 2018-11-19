class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int

        res = 0
        ls = len(heights)
        for i in range(0, ls):
            h = heights[i]
            for j in range(i,ls):
                h = min(h,heights[j])
                res = max(res, (j-i+1)*h)

        return res
        """

        heights.append(0)
        stack = []
        i = 0
        result = 0
        while i < len(heights):
            if not stack or heights[stack[-1]] < heights[i]:
                stack.append(i)
                i += 1
            else:
                num = stack.pop(-1)
                result = max(result, heights[num] * (i - stack[-1] - 1 if stack else i))
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))