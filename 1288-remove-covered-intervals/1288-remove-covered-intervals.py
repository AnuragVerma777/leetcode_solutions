class Solution(object):
    def removeCoveredIntervals(self, intervals):
        
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))

        count = 0
        farthest_end = 0

        for start, end in intervals:
            
            if end > farthest_end:
                count += 1
                farthest_end = end

        return count



        