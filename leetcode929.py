class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = []
        for email in emails:
            l = email.split('@')
            local = l[0]
            domain = l[1]
            t_local = ''
            for x in local:
                if x != '.' and x != '+':
                    t_local += x
                elif x == '+':
                    break
            if t_local+'@'+domain not in res:
                res.append(t_local+'@'+domain)
        return len(res)