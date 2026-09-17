class Solution(object):
    def maxSubArray(self, nums):
     curr=nums[0]
     maxi=nums[0]
     for i in range(1,len(nums)):
        curr = max(nums[i],curr+nums[i])
        maxi = max(maxi,curr)
     return maxi   


