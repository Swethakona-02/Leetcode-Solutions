class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        sA=0
        for i in range(len(nums)):
            start=max(0,i-nums[i])
            sA+=sum(nums[start:i+1])
        return sA
        
