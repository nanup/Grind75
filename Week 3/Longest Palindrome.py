class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length = 0
        
        dict = {}
        
        for ch in s:
            if ch in dict:
                dict[ch] += 1
            else:
                dict[ch] = 1
                
        for key in dict:
            if dict[key] % 2 == 0:
                length += dict[key]
            elif (dict[key] - 1) % 2 == 0:
                length += dict[key] - 1
        
        if length < len(s):
            length += 1
        
        return length