class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum=nums[0]
        i=1
        while i<len(nums) and nums[i]==nums[i-1]+1:
            sum+=nums[i]
            i+=1
        while sum in nums:
            sum+=1
        return sum

        
