class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new = ''
        for x in s:
            if (ord(x)>=ord('a') and ord(x) <= ord('z')) or (ord(x)>=ord('0') and ord(x) <= ord('9')):
                new += x
        ls = len(new)
        j = ls//2-1
        if ls % 2 == 1:
            k = j+2
        else:
            k = j+1
        while j >=0 and k < ls:
            if new[j] != new[k]:
                return False
            j-=1
            k+=1
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("OP"))