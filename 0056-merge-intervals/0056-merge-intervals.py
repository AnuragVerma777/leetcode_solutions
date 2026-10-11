class Solution(object):
    def merge(self, intervals):
       intervals.sort()
       s,e=intervals[0]
       res=[]
       for start ,end in intervals[1:]:
         if start<=e:
            e=max(e,end)

         else :
            res.append([s,e])
            s, e = start, end
       res.append([s, e])   
       
       return res