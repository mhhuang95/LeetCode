import random
class RandomizedSet(object):
    def __init__(self):
        self._map = {}

    def insert(self, val):
        if val not in self._map:
            self._map[val] = True
            return True
        return False

    def remove(self, val):
        if val in self._map:
            del self._map[val]
            return True
        return False

    def getRandom(self):
        return random.choice(self._map.keys())



        # Your RandomizedSet object will be instantiated and called as such:
        # obj = RandomizedSet()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()