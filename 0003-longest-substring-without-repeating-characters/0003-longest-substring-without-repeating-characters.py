class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        ans = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            ans = max(ans, right - left + 1)

        return ans