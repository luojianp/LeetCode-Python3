# ex2tron's blog:
# http://ex2tron.wang


# 这题不会，别人的代码：


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)
        global_max, local_max = 0, 0
        for x in nums:
            local_max = max(0, local_max + x)
            global_max = max(global_max, local_max)
        return global_max


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
