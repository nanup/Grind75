class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        currentSum = 0
        
        for num in nums:
            if currentSum < 0:
                currentSum = 0
                
            currentSum += num
            
            maxSum = max(maxSum, currentSum)
            
        return maxSum