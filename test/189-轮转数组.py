# nums = [1,2,3,4,5,6,7]
# k = 3

nums = [1,2]
k = 3

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 定义实际需要调整的位数，因为k值可能大于实际的数组长度，比如数组有3个元素，k值为5，实际上跟k值为2的效果一致
        curr_step = k%len(nums)
        print(curr_step)
        nums[:] = nums[-curr_step:] + nums[:-curr_step]
        print(nums)


solution = Solution()
print(solution.rotate(nums,k))
#solution.rotate(nums,k)