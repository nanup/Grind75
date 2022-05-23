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

# Dynamic Programming

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        subArraySums = [0] * len(nums)
        subArraySums[0], maxSum = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            subArraySums[i] = max(nums[i], subArraySums[i - 1] + nums[i])
            maxSum = max(maxSum, subArraySums[i])
            
        return maxSum