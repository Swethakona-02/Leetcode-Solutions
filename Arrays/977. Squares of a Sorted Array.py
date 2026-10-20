class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[i]**2)
        ans.sort()
        return ans
