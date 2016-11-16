from collections import defaultdict

class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.data = defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.data[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        data = self.data
        for item in data:
            if value - item in data:
                if value - item == item:
                    if self.data[item] > 1:
                        return True
                else:
                    return True
        return False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)