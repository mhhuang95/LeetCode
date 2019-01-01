
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 0
        for i in range(1,n):
            if knows(k,i):
                k = i
        if any(not knows(i,k) or knows(k,i) for i in range(n) if i != k):
            return -1
        return k