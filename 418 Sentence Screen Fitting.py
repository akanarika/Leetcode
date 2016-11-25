class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        nums = []
        for i, word in enumerate(sentence):
            curr_left = cols
            idx = 0
            curr_len = len(sentence[i])
            while curr_left >= curr_len:
                curr_left -= curr_len + 1
                idx += 1
                curr_len = len(sentence[(idx+i)%len(sentence)])
            nums.append(idx)
            
        idx = 0
        cnt = 0
        for _ in range(rows):
            cnt += nums[idx]
            idx = cnt % len(sentence)
        
        return cnt/len(sentence)        
        