from typing import List

nums = [3,4,-1,1]
# [1,-1,3,4]
#nums = [7,8,9,11,12]

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        # sort() 的时间复杂度已经到了O(nlogn)。这种写法的空间复杂度为 O(1)
        nums.sort()
        min_dt = 1
        for i in range(len(nums)):
            if nums[i] <= 0:
                continue
            else:
                if min_dt < nums[i]:
                    break
                elif min_dt == nums[i]:
                    min_dt += 1
                else:
                    continue
        return min_dt
        """
        """
        这种写法的逻辑就是基于：
        缺失值一定在[1~n+1]这个区间内，缺失值为n+1的情况下，每个值x对应的自己的索引应该是x-1，如果每个值都跟自己应该对应的下标相对，则值为n+1
        所以可以假定该值就为n+1，将每个值调换到自己应该在的位置之后再遍历，如果存在值跟索引对不上的情况，索引值+1就是相应的缺失值
        """
        n = len(nums)
        #首轮遍历，目的在于将每个值放到应该存在的位置
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        # 第二轮遍历，2应该在索引1,3应该在索引2，如果一个值所以不是值-1，那这个值前面一定存在缺失值为i+1
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1



souluton = Solution()
print(souluton.firstMissingPositive(nums))