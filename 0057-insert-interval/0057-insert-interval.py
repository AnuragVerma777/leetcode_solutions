class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        result=[]
        intervals.sort()
        start,end =intervals[0]
        for s,e in intervals[1:]:
           if s<=end:
            end = max(end ,e) 
           else:
            result.append([start,end])
            start,end=s,e
        result.append([start,end])
        return result       