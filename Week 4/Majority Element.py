class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        
        majNum = None
        majNumCount = 0
        
        for num in nums:
            if num in dict:
                dict[num] += 1
                
            else:
                dict[num] = 1
                
        for num in dict:
            if dict[num] > len(nums) // 2 and dict[num] > majNumCount:
                majNum = num

        return majNum