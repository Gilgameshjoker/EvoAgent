from typing import List

#intervals = [[1,3],[2,6],[8,10],[15,18],[4,9]]
intervals = [[1,9],[2,5],[19,20],[10,11],[12,20],[0,3],[0,1],[0,2]]

#intervals = [[1,4],[4,5]]



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        #print(intervals)
        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:  # merged[-1][1]中，-1表示组末的第一个元素
                merged.append(interval)
            else:
                # 否则与上一区间合并
                merged[-1][1] = max(merged[-1][1], interval[1]) # merged[]数组中的最后一个元素的右界取更大的一个值
        return merged



solution = Solution()
print(solution.merge(intervals))