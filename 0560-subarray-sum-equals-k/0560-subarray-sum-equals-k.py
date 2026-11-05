class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        total = 0
        seen = {0: 1}              # running sum 0 has appeared once (empty start)

        for num in nums:
            total += num           # running sum so far

            need = total - k       # earlier sum that would leave a subarray of sum k
            if need in seen:
                count += seen[need]

            seen[total] = seen.get(total, 0) + 1

        return count