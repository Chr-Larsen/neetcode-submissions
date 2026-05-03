class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        while i < len(nums):
            prod = 1
            j = 0
            while j < len(nums):
                if j != i:
                    prod *= nums[j]
                j += 1
            res.append(prod)
            i += 1

        return res
            
        
