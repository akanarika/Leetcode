from collections import defaultdict

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_id = defaultdict(list) #vals=>id
        self.id_val = {} #id => vals
        self.length = 0 #length


    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.length += 1
        self.id_val[self.length] = val
        if val in self.val_id:
            self.val_id[val].append(self.length)
            return False
        else:
            self.val_id[val].append(self.length)
            return True
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.val_id and self.val_id[val]:
            id = self.val_id[val].pop()
            del self.id_val[id]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        id = random.sample(self.id_val.keys(), 1)
        return self.id_val[id[0]]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()