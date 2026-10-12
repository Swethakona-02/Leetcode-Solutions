class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        spcl=0
        for i in range(1,n+1):
            if n%i==0:
                spcl+=nums[i-1]**2
        return spcl
        

        
