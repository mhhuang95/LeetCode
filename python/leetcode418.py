class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = ' '.join(sentence)+' '
        start, ls = 0, len(s)
        for i in range(rows):
            start += cols
            while s[start % ls] != ' ':
                start -= 1
            start += 1
        return start // ls

if __name__ == "__main__":
    s = Solution()
    print(s.wordsTyping(["hello","world"],2,8))