class Solution:
    def maxArea(self, height: List[int]) -> int:
        start,end=0,len(height)-1
        max_area=0
        while start<end:
            max_area=max(max_area, min(height[start],height[end])*(end-start))
            if height[start]>=height[end]:
                end-=1
            else:
                start+=1
        return max_area
