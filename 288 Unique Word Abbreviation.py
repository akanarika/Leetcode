from collections import defaultdict

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.d = defaultdict(set)
        for item in dictionary:
            if len(item) > 2:
                abbr = item[0] + str(len(item)) + item[-1]
                self.d[abbr].add(item)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = ""
        if len(word) > 2:
            abbr = word[0] + str(len(word)) + word[-1]
        return abbr not in self.d or self.d[abbr] == set([word])


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")