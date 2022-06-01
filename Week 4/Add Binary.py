class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j, carry = len(a) - 1, len(b) - 1, 0
        
        res = ""
        
        while (i >= 0 or j >= 0):
            sum = carry
            
            if i >= 0: sum += ord(a[i]) - ord("0")
            if j >= 0: sum += ord(b[j]) - ord("0")
            
            i, j = i - 1, j - 1
            
            carry = 1 if sum > 1 else 0;
            
            res = str(sum % 2) + res
            
        if carry != 0: res = str(carry) + res
            
        return res