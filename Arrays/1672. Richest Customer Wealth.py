class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        m=len(accounts)
        max_wealth=0
        for i in range(m):
            wealth=0
            for j in range(len(accounts[i])):
                wealth+=accounts[i][j]
            max_wealth=max(max_wealth,wealth)
        return max_wealth

        
