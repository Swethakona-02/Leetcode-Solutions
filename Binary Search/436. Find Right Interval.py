class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        starts=[]
        for i in range(len(intervals)):
            starts.append((intervals[i][0],i))
        starts.sort()
        ans=[]
        for start,end in intervals:
            left=0
            right=len(starts)-1
            res=-1
            while left<=right:
                mid=(left+right)//2
                if starts[mid][0]>=end:
                    res=starts[mid][1]
                    right=mid-1
                else:
                    left=mid+1
            ans.append(res)
        return ans
