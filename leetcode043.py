class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        n1 = 0
        n2 = 0
        res = ''
        for i in range(l1):
            n1 = n1 * 10 + ord(num1[i])- ord('0')
        for i in range(l2):
            n2 = n2 * 10 + ord(num2[i]) - ord('0')
        pro = n1*n2
        if pro == 0:
            return '0'
        while pro > 0:
            x = pro % 10
            pro = pro // 10
            res = str(x) + res
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.multiply('123','456'))
