class Solution(object):
    def eraseOverlapIntervals(self, intervals):
     
        intervals.sort()
        count = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            curr_end = intervals[i][1]

            if start < end:
                # overlap → remove the interval ending later
                count += 1
                end = min(end, curr_end)
            else:
                end = curr_end

        return count
        
