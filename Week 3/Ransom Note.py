class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote = Solution().hashify(ransomNote)
        magazine = Solution().hashify(magazine)
        
        for key in ransomNote:
            if key in magazine and magazine[key] >= ransomNote[key]:
                continue
            else:
                return False
        return True
        
    def hashify(self, aString):
        hashMap = {}
        
        for ch in aString:
            if ch in hashMap:
                hashMap[ch] += 1
            else:
                hashMap[ch] = 1
                
        return hashMap