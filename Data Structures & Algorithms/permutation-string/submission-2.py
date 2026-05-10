class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)
        l = 0
        r = 0
        for c in s1:
            count[c] += 1
        
        while r < len(s2):
            if s2[r] in count and count[s2[r]] > 0:
                count[s2[r]] -= 1
                r += 1
                if all(v == 0 for v in count.values()):
                    return True
            else:
                if s2[l] in count:
                    count[s2[l]] += 1
                l += 1
                if l >= r:
                    r = l
        
        return False