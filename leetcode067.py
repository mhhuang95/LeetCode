class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        a = int(a)
        b = int(b)
        sum = str(a+b)
        ls = len(sum)
        curr = 0
        for i in range(ls-1, -1,-1):
            if int(sum[i])+curr == 0:
                res = '0'+res
            elif int(sum[i]) + curr == 1:
                curr = 0
                res = '1'+res
            elif int(sum[i]) + curr == 2:
                curr = 1
                res = '0' + res
            else:
                curr = 1
                res = '1' + res
        if curr == 1:
            res = '1' + res
        return res

