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
        
s = "9,8"
print(Solution().isPalindrome(s))