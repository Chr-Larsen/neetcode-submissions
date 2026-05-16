class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix[0]) - 1
        row = len(matrix) - 1

        for i in range(len(matrix)):
            if matrix[i][0] > target and i > 0:
                row = i-1
                break
            elif matrix[i][0] > target and i == 0:
                return False
        
        while low <= high:
            mid = low + (high - low)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
            
        return False