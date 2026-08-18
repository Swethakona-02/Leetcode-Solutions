class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        d = {}
        for i in range(len(nums) - k + 1):
            seen = set()
            for j in range(i, i + k):
                seen.add(nums[j])
            for num in seen:
                if num in d:
                    d[num] += 1
                else:
                    d[num] = 1
        ans = -1
        for num in d:
            if d[num] == 1 and num > ans:
                ans = num
        return ans
