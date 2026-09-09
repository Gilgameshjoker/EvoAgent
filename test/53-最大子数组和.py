from typing import List

nums = [-2,1,-3,4,-1,2,1,-5,4]


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #  第一种写法，时间复杂度为O(N)，空间复杂度为O(N)
        """
        size = len(nums)
        if size == 0:
            return 0

        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1,size):
            if dp[i-1] >= 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)
        """

        # 第二种写法，时间复杂度O(N)，空间复杂度O(1)
        size = len(nums)
        pre = 0  # 以nums[i]为末尾的数值最大的和
        res = nums[0]
        for i in range(size):
            pre = max(nums[i],pre + nums[i])
            res = max(res,pre)
        return res

solution = Solution()
print(solution.maxSubArray(nums))