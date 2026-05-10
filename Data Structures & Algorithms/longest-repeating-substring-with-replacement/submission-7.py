class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        i = 0
        maxCount = 0
        maxFreq = 0

        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1
            maxFreq = max(maxFreq, count[s[j]])

            # window size - most frequent char > k means we need to shrink
            while (j - i + 1) - maxFreq > k:
                count[s[i]] -= 1
                i += 1

            maxCount = max(maxCount, j - i + 1)

        return maxCount