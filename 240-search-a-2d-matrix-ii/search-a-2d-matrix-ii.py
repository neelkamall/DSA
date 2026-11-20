class Solution(object):
    def searchMatrix(self, matrix, target):
        
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1  # Start from top-right

        while row < m and col >= 0:
            curr = matrix[row][col]
            if curr == target:
                return True
            elif curr > target:
                col -= 1
            else:
                row += 1

        return False
        