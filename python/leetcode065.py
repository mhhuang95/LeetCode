class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if len(s) == 0:
            return False
        if 'e' in s:
            p = s.split('e')
            if len(p) != 2:
                return False
            for i, x in enumerate(p):
                if x == '':
                    return False
                if not self.sub_num(i,x):
                    return False
        else:
            if not self.sub_num(0,s):
                return False
        return True


    def sub_num(self, i,s):
        if s[0] == '+' or s[0]== '-':
            s = s[1:]
        if len(s) == 0:
            return False
        if '.' in s:
            if i == 0:
                p = s.split('.')
                if len(p) != 2:
                    return False

                if p[0] =='' and p[1] == '':
                    return False
                for x in p:
                    if x == '':
                        continue
                    if not self.all_num(x):
                        return False
            if i == 1:
                return False
        else:
            if not self.all_num(s):
                return False
        return True

    def all_num(self,x):
        ls = len(x)
        flag = 0
        for r in x:
            if ord(r) < ord('0') or ord(r) > ord('9'):
                flag = 1
        if flag:
            return False
        else:
            return True

if __name__ == "__main__":
    s = Solution()
    print(s.isNumber('.1'))