class Solution(object):
    def spiralOrder(self, mat):
        m = len(mat)
        n = len(mat[0])
        s_row = 0
        s_col = 0
        e_row = m-1
        e_col = n-1
        ans = []

        while s_row <= e_row and s_col <= e_col:
            for j in range(s_col, e_col + 1):
                ans.append(mat[s_row][j])
            for i in range(s_row + 1, e_row + 1):
                ans.append(mat[i][e_col])
            for j in range(e_col -1, s_col - 1, -1):
                if s_row == e_row:
                    break
                ans.append(mat[e_row][j])
            for i in range(e_row -1 , s_row, -1):
                if s_col == e_col:
                    break
                ans.append(mat[i][s_col])   

            s_row += 1
            e_row -= 1
            s_col += 1
            e_col -= 1

        return ans                 
        