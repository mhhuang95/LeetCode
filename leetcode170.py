class TwoSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.nums[number] = self.nums.get(number, 0) +1


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.nums:
            if value - key in self.nums and self.nums[key]-(value-key == key):
                return True
        return False


        # Your TwoSum object will be instantiated and called as such:
        # obj = TwoSum()
        # obj.add(number)
        # param_2 = obj.find(value)