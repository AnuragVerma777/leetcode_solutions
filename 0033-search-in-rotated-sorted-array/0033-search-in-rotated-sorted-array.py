class Solution(object):

   def search(self,nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        # Left half sorted hai
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1      # target left mein hai
            else:
                low = mid + 1       # target right mein hai

        # Right half sorted hai
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1       # target right mein hai
            else:
                high = mid - 1      # target left mein hai

    return -1