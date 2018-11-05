class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        p = path.split('/')
        ls = len(p)
        while ls > 0:
            ls = ls-1
            if p[ls] == '':
                p.pop(ls)
        ls = len(p)
        i = 0
        while i < ls:

            if p[i] == '.':
                p.pop(i)
                ls -= 1
            elif i > 0 and p[i] == '..':
                p.pop(i)
                p.pop(i-1)
                i = i - 1
                ls -= 2
            elif i == 0 and p[i] == '..':
                p.pop(i)
                ls -=1
            else:
                i = i + 1
        p.insert(0,'')
        if len(p) == 1:
            p.append('')
        return '/'.join(p)

if __name__ == "__main__":
    s = Solution()
    print(s.simplifyPath("/a/./b/../../c/"))