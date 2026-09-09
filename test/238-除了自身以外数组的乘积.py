from typing import List

nums = [-1,1,0,-3,3]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """ 分别计算左右子区间大小的方式
        L = [0] * len(nums)
        R = [0] * len(nums)
        answer = [0] * len(nums)
        L[0] = 1
        for i in range(1,len(nums)):
            L[i] = nums[i-1] * L[i-1]
        R[len(nums)-1] = 1
        for i in reversed(range(len(nums) - 1)):
            R[i] = nums[i+1] * R[i+1]
        for i in range(len(nums)):
            answer[i] = L[i] * R[i]
        return answer
        """

        # 先计算i左边的乘积，然后动态计算右边的乘积并赋值给最终结果
        length = len(nums)
        answer = [0] * length

        ## answer表示i左侧所有数字的乘积
        ## 因为索引0的元素左侧没有元素，所以answer[0]= 1
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i-1] * answer[i-1]

        # R为右侧所有元素的乘积
        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer


solution = Solution()
print(solution.productExceptSelf(nums))