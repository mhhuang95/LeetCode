class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = ''
        if numerator/denominator<0:
            res += '-'
        numerator, denominator = abs(numerator), abs(denominator)
        integer, remainder = divmod(numerator, denominator)
        res += str(integer)
        if remainder!= 0:
            res+= '.'
        i = len(res)
        table = {}
        while remainder != 0:
            if remainder not in table:
                table[remainder] = i
            else:
                i =table[remainder]
                res = res[:i]+ '('+res[i:]+')'
                return res
            remainder*= 10
            res += str(remainder//denominator)
            remainder %= denominator
            i+=1
        return res