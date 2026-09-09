from typing import List


matrix = [[1,1,1],[1,0,1],[1,1,1]]

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        # 这种是最简单的实现方法，通过两次双重循环实现。时间复杂度为O(mn)，空间复杂度为O(m+n)
        m,n = len(matrix),len(matrix[0])
        row,col = [False]*m,[False]*n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        """
        """ 这种方式就是把第一行跟第一列的做单独处理，替代第一种方法中的标记数组，空间优化到O(1)
        # 优化空间复杂度为O(1)，时间复杂度保持不变
        m,n = len(matrix),len(matrix[0])
        # any是判断是否有任意一个满足条件，如果有则返回True。这里判断矩阵第0列是否至少有一个0，如果有返回True，否则为False
        flag_col0 = any(matrix[i][0] == 0 for i in range(m))
        flag_row0 = any(matrix[0][i] == 0 for i in range(n))

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0

        if flag_row0:
            for j in range(n):
                matrix[0][j] = 0
        """


solution = Solution()
print(solution.setZeroes(matrix))