class Solution(object):
    def minWindow(self, s, t):
   

        if not s or not t or len(t) > len(s):
            return ""

        need = Counter(t)        # how many of each char we still need
        missing = len(t)         # total chars still missing from the window
        left = 0
        best_start, best_len = 0, float('inf')

        for right, ch in enumerate(s):
            # expand the window by including s[right]
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            # window now has everything from t -> try to shrink it
            if missing == 0:
                # skip chars on the left that aren't needed (or are extra)
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                # record the best window
                if right - left + 1 < best_len:
                    best_start, best_len = left, right - left + 1

                # drop s[left] so we can look for the next valid window
                need[s[left]] += 1
                missing += 1
                left += 1

        return "" if best_len == float('inf') else s[best_start:best_start + best_len]