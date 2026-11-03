class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mE=max(nums)
        cnt=0
        for i in range(len(nums)):
            cnt+=mE-nums[i]
        return cnt
