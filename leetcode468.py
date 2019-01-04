class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP and self.isvalidv4(IP):
            return "IPv4"
        if ':' in IP and self.isvalidv6(IP):
            return "IPv6"
        return "Neither"

    def isvalidv4(self, IP):
        ips = IP.split('.')
        if len(ips) !=4:
            return False
        for x in ips:
            if len(x) == 0:
                return False
            if len(x) != 1 and x[0] == '0':
                return False
            for i in x:
                if i not in ['0','1','2','3','4','5','6','7','8','9']:
                    return False
            if int(x)>255:
                return False
        return True

    def isvalidv6(self, IP):
        ips = IP.split(':')
        if len(ips) != 8:
            return False
        for x in ips:
            x = x.lower()
            if len(x) == 0 or len(x) >4:
                return False
            for i in x:
                if i not in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
                    return False
        return True