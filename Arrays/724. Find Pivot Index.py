class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        totalSum=0
        for i in range(len(nums)):
            totalSum+=nums[i]
        leftSum=0
        for i in range(len(nums)):
            rightSum=totalSum-leftSum-nums[i]
            if leftSum==rightSum:
                return i
            leftSum+=nums[i]
        return -1
        
