class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [0]*(len(nums) - (k - 1))
        window = [0]*k
        maxTemp = 0
        maxTempIdx = 0

        for i in range(k):
            window[i] = nums[i]
        maxTemp = max(window)
        maxTempIdx = window.index(maxTemp)
        res[0] = maxTemp

        for i in range(k, len(nums)):
            if maxTempIdx != 0:
                if nums[i] >= maxTemp:
                    maxTempIdx = k-1
                    maxTemp = nums[i]
                else:
                    maxTempIdx -= 1
                window.pop(0)
                window.append(nums[i])
            else:
                window.pop(0)
                window.append(nums[i])
                maxTemp = max(window)
                maxTempIdx = window.index(maxTemp)
            res[i - k + 1] = maxTemp

        return res