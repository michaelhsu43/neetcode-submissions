class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        ## binary search the first column, then the row
            
        left, right = 0, m - 1
        while left < right:
            mid = (left + right) // 2
            if matrix[mid][n - 1] < target:
                left = mid + 1
            else:
                right = mid
        
        row = left

        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid

        print(row, left)
        
        return matrix[row][left] == target


