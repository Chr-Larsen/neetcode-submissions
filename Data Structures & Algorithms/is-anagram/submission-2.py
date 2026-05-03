class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sorted_s = sorted(s)
            sorted_t = sorted(t)
            for i in range(len(s)):
                if sorted_s[i] != sorted_t[i]:
                    return False
            return True
        return False