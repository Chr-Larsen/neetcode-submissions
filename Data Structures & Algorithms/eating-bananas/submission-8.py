class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high - low) // 2
            time = sum(math.ceil(p/mid) for p in piles)

            if time <= h:
                high = mid - 1
            else:
                low = mid + 1
        
        return low