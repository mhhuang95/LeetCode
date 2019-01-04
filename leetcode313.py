class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res = [1]
        dic = {}
        for x in primes:
            dic[x] = 0
        i = 1
        while len(res) < n:
            temp = []
            for x in dic:
                while res[dic[x]] * x <= res[-1]:
                    dic[x] += 1
                temp.append(res[dic[x]] * x)
            res.append(min(temp))
        return res[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.nthSuperUglyNumber(12,[2,7,13,19]))