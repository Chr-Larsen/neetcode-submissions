class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = 0

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        mid = l
        l = 0
        r = len(nums) - 1

        if target > nums[r]:
            r = mid
        else:
            l = mid
        
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        if nums[l] == target:
            return l
        else:
            return -1