class Solution():
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ls = len(height)
        low = 0
        high = ls - 1
        l = min(height[low], height[high])
        max_v = l * (high - low)
        while low < high:
            while height[low] < l and low < ls:
                low = low + 1
            while height[high] < l and high > 0:
                high = high - 1
            if low > high:
                break
            m = min(height[low], height[high])
            if m * (high - low) > max_v:
                max_v = m * (high - low)
                l = m
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return max_v