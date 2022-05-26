class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        distinctWays = {}
        
        i = 0
        
        while i <= n:
            if i >= 2:
                distinctWays[i] = distinctWays[i-1] + distinctWays[i-2]
            else:
                distinctWays[i] = 1
            
            i += 1
            
        return distinctWays[n]