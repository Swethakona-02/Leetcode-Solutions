class Solution:
    def checkDivisibility(self, n: int) -> bool:
        ds=0
        dp=1
        for digit in str(n):
            digit=int(digit)
            ds+=digit
            dp*=digit
        if n%(ds+dp)==0:
            return True
        return False
        
