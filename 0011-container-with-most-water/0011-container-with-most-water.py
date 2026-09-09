class Solution(object):
    def maxArea(self, height):
        count=0
        l = 0
        r = len(height)-1
        
        while l < r:
            area = min(height[l],height[r])*(r-l)
            count = max(area,count)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1

        return count