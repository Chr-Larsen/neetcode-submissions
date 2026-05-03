class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                k = (nums[i]+nums[j])*-1
                if k in seen:
                    tripset = sorted([nums[i], nums[j], k])
                    if tripset not in res:
                        res.append(tripset)
            seen.add(nums[i])
        return res