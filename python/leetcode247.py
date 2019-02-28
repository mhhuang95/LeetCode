class Solution(object):
    def findStrobogrammatic1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dic = {'1': '1', '0': '0', '8': '8', '6': '9', '9': '6'}
        cen = {'1': '1', '0': '0', '8': '8'}

        def helper(n):
            if n == 1:
                res = []
                for key in cen:
                    if key != '0':
                        res.append(cen[key])
                return res
            elif n == 2:
                res = []
                for key in dic:
                    res.append(key+dic[key])
                return res
            else:
                res = helper(n-2)
                temp = []
                for x in res:
                    for key in dic:
                        temp.append(key+x+dic[key])
                ls = len(temp)
                i = 0
                while i < ls:
                    if temp[i][0] == '0':
                        temp.pop(i)
                        ls -= 1
                    i+=1
                return temp

        return helper(n)

    def findStrobogrammatic(self, n):
        oddmid = ['0','1','8']
        evenmid = ['00','11','88','69','96']
        if n == 1:
            return oddmid
        if n == 2:
            return evenmid[1:]
        if n%2:
            pre, mid = self.findStrobogrammatic(n-1), oddmid
        else:
            pre, mid = self.findStrobogrammatic(n-2), evenmid
        premid = (n-1)//2
        return [p[:premid] + c + p[premid:] for c in mid for p in pre]
