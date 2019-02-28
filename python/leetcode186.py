class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        self.reversed(str, 0, len(str) -1)

        j = 0
        for i in range(len(str)):
            if str[i] == " ":
                self.reversed(str, j, i-1)
                j = i+1
            elif i == len(str)-1:
                self.reversed(str, j,i)

    def reversed(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1