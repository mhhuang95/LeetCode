class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        if l2 < l1:
            return self.addStrings(num2,num1)
        curr = 0
        res = ''
        for i in range(l1):
            tmp = curr + int(num2[-i-1]) + int(num1[-i-1])
            if tmp >=10:
                curr = 1
                tmp -= 10
            else:
                curr = 0
            res = str(tmp) + res
        if l2 > l1:
            res = str(int(num2[:l2-l1])+curr) + res
        elif curr == 1:
            res = '1' + res
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.addStrings("98","9"))