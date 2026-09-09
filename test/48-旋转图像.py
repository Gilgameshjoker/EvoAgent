"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
"""
from typing import List

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        # 这个问题最重要的是理解，第i行第j列的元素，旋转90度之后出现在倒数第i列的第j个位置
        n = len(matrix)
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n-i-1] = matrix[i][j]
        matrix[:] = matrix_new
        return matrix
        """
        # 也可以使用两次翻转得到结果，先使用一次水平轴翻转，再使用一次对角线翻转，也能获取到旋转90度的效果
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix



solution = Solution()
print(solution.rotate(matrix))