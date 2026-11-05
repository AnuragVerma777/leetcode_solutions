class Solution(object):
    def twoSum(self, nums, target):
        seen = {}                      # value -> index
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
        return []                      # problem guarantees a solution