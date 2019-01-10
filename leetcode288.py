class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dic = dictionary
        self.abb = {}
        for x in dictionary:
            if len(x) <=2:
                if x not in self.abb:
                    self.abb[x] = self.abb.get(x,0)+1
            else:
                self.abb[x[0] + str(len(x)-2) + x[-1]] = self.abb.get(x[0] + str(len(x)-2) + x[-1],0) +1


    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)<=2:
            abb = word
        else:
            abb = word[0] + str(len(word)-2) + word[-1]
        if word in self.dic:
            return self.abb[abb] - 1 == 0
        else:
            return abb not in self.abb



if __name__ == "__main__":
    s = ValidWordAbbr(["hello"])
    print(s.abb)
    print(s.isUnique("hello"))


        # Your ValidWordAbbr object will be instantiated and called as such:
        # obj = ValidWordAbbr(dictionary)
        # param_1 = obj.isUnique(word)