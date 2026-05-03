class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset = set(nums)
        runs = []
        for num in numset:
            run = 1
            while True:
                if num+1 not in numset:
                    break
                run += 1
                num += 1
            runs.append(run)
        return max(runs)
            