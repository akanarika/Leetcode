class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
            
        l = [True] * n
        l[0] = False
        l[1] = False
        count = 0
        i = 2
        while i * i < n:
            if l[i]:
                if self.isPrime(i):
                    l[i] = True
                    j = i * 2
                    while j < n:
                        l[j] = False
                        j += i
            i += 1

        return sum(l)
        
    def isPrime(self, x):
        if x == 2:
            return True
        i = 2
        while i * i < x:
            if x % i == 0:
                return False
            i += 1
        return True
        