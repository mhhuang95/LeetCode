map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        l = len(digits)
        if l == 0:
            return []
        if l == 1:
            return [x for x in map[digits[0]]]
        else:
            res = []
            s = map[digits[0]]
            for x in s:
                temp = self.letterCombinations(digits[1:])
                for t in temp:
                    res.append(x+t)
            return res


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations('23'))