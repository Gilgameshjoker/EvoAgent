import bisect
from typing import List

# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 5

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        方法一：最蠢的方法：全体遍历   时间复杂度O(mn)，空间复杂度O(1)
        :param matrix:
        :param target:
        :return:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False
        """
        """
        #第二种方法：每一行都是升序排序，对每一行使用二分查找(也很蠢)  时间复杂度O(mlogn)，空间复杂度O(1)
        for row in matrix:
            idx = bisect.bisect_left(row,target)  ## 返回在升序列表中target应当插入的位置，保持原有列表升序不变。如果已存在，返回第一个元素位置
            if idx < len(row) and row[idx] == target:
                return True
        return False
        """
        # 这种方法给我一开始想的类似，但是我没想到应当从右上角第一个元素开始搜素。当target小于当前元素时，列往左移；当target大于当前元素时，行往下移
        m,n = len(matrix),len(matrix[0])
        x,y = 0,n-1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False


solutuon = Solution()
print(solutuon.searchMatrix(matrix,target))