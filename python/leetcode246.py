class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {'1':'1','0':'0','8':'8','6':'9','9':'6'}
        ls = len(num)
        for i in range((ls+1)//2):
            if num[i] not in dic or dic[num[i]] != num[ls-1-i]:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isStrobogrammatic('962'))
