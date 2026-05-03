class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        prod = 1
        res = []
        while i < len(nums):
            j = 0
            while j < len(nums):
                if j != i:
                    prod *= nums[j]
                j += 1
            res.append(prod)
            prod = 1
            i += 1

        return res
            
        
