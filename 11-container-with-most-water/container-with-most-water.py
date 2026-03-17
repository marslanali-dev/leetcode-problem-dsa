class Solution:
    def maxArea(self, height: List[int]) -> int:
        output=0
        n=len(height)-1
        start=0
        while n-start != 0:
            area=min(height[start],height[n])* (n - start)
            output=max(area,output)
            if height[start]<=height[n]:
                start+=1
            else:
                n-=1
        return output