class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        length = len(heights)

        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][1]:
                index, height = stack.pop()
                width = i - index
                area = max(area, height*width)
                start = index
            stack.append((start, heights[i]))

        while stack:
            index, height = stack.pop()
            width = length - index
            area = max(area, height*width)

        return area