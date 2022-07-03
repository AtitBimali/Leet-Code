#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i,elem in enumerate(nums):
            if target-elem in values:
                return[values[target-elem],i]
            else:
                values[elem]=i
            
        
        
