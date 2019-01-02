class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold, not_hold, not_hold_cooldown = float("-inf"), 0, float("-inf")
        for p in prices:
            hold, not_hold, not_hold_cooldown = max(hold, not_hold - p), max(not_hold, not_hold_cooldown), hold+p
        return max(not_hold_cooldown, not_hold)
