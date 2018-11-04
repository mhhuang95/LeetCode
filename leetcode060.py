import math
class Solution:
    '''
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        l = [i+1 for i in range(n)]

        for n in range(k-1):
            l = self.next_num(l)
        res = ''
        for x in l:
            res += str(x)
        return res

    def next_num(self, l):
        ls = len(l)
        i = ls-1
        while l[i-1]>l[i]:
            i -= 1
        j = i
        temp = l[i-1]
        while j < ls and l[j] > temp:
            j = j + 1
        l[j-1], l[i-1] = l[i-1], l[j-1]
        k = l[i:]
        k.sort()
        l[i:]=k[:]
        return l
        '''

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        nums = list(range(1,n+1))
        k = k - 1
        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            res += str(nums[index])
            nums.remove(nums[index])
        return res

    def fac(self,l):
        if l == 1:
            return 1
        return l*self.fac(l-1)

if __name__=="__main__":
    s = Solution()
    print(s.getPermutation(9, 278082))