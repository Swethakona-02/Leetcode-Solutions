class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum = 0
            n = nums[i]

            while n > 0:
                digit = n % 10
                sum += digit
                n //= 10

            if i == sum:
                return i

        return -1
