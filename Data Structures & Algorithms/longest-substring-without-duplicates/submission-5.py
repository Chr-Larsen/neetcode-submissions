class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        i = 0
        maxCount = 0
        while i < len(s) and len(s) - i > maxCount:
            count = 0
            j = i
            while j < len(s) and s[j] not in seen:
                seen.append(s[j])
                j += 1
                count += 1
            maxCount = max(maxCount, count)
            if j < len(s):
                i += seen.index(s[j]) + 1
            else:
                break
            seen.clear()
        
        return maxCount