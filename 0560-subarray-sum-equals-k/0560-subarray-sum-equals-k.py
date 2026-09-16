class Solution(object):
    def subarraySum(self, nums, k):
     count = 0
     prefix = 0
     seen = {0: 1}
     for num in nums :
        prefix += num
        if prefix - k in seen:
           count += seen[prefix-k]
        seen[prefix] = seen.get(prefix,0)+1

     return count               
