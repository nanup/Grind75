class Solution(object):
    def twoSum(self, nums, target):
        idxDict = {}
        for i, num in enumerate(nums):
            if target - num in idxDict:
                return [idxDict[target - num], i]
            idxDict[num] = i