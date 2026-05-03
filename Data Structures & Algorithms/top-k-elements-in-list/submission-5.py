class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        resultList = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for i in range(k):
            maxNum = max(count, key=lambda x: count[x])
            resultList.append(maxNum)
            count.pop(maxNum)
        return resultList