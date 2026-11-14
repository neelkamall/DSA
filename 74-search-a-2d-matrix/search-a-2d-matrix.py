class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix) 
        n = len(matrix[0])
        str_row = 0
        end_row = m - 1

        while str_row <= end_row:
            mid_row = str_row + (end_row - str_row) // 2
            if target >= matrix[mid_row][0] and matrix[mid_row][n-1] >= target:
                left = 0
                right = n-1
                while left <= right:
                    mid = left + (right - left) // 2
                    if target == matrix[mid_row][mid]:
                        return True
                    elif target > matrix[mid_row][mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False                
            elif target > matrix[mid_row][n-1]:
                str_row = mid_row + 1
            else:
                end_row = mid_row - 1
        return False                

        