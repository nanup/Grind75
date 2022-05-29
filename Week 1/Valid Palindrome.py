class Solution(object):
    def isPalindrome(self, s):
        tokenList = 'abcdefghijklmnopqrstuvwxyz0123456789'
        if not s:
            return True
        s = s.lower()
        k = len(s)
        i = 0
        j = k - i - 1
        while i < j:
            while s[i] not in tokenList:
                if i > k - 1 or i > j - 1:
                    break
                i += 1
            while s[j] not in tokenList:
                if j < 1 or j < i + 1:
                    break
                j -= 1
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

# second try
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = Solution().alterString(s)
        print(s)
        return Solution().isPalindromeA(s)
        
        
    
    def alterString(self, aString):
        alteredString = []
        
        for ch in aString:
            if ch.isalnum():
                alteredString.append(ch.lower())
            
        return "".join(alteredString)
    
    def isPalindromeA(self, aString):
        i = 0
        j = len(aString) - i - 1
        
        while i <= j:
            j = len(aString) - i - 1
            
            if aString[i] != aString[j]:
                return False
            
            i += 1
            
        return True
        
s = "race a car"
print(Solution().isPalindrome(s))