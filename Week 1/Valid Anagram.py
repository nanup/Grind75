class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dictS = Solution().dictionarise(s)
        dictT = Solution().dictionarise(t)
        
        for i in dictS.keys():
            try:
                if dictS[i] == dictT[i]:
                    continue
                return False
            except:
                return False
            
        return True
        
    def dictionarise(self, aString):
        dict = {}
        for ch in aString:
            if ch in dict:
                dict[ch] += 1
            else:
                dict[ch] = 1
        return dict

print(Solution().isAnagram('aacc', 'ccac'))