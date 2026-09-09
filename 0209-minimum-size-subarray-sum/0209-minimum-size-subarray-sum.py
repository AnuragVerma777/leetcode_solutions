class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        c = 0
        ans = float('inf')
        for right in range(len(nums)):
            c += nums[right]
            while c >= target:
                ans = min(right - l + 1, ans)
                c -= nums[l]
                l += 1
        if ans == float('inf'):
            return 0
        return ans


