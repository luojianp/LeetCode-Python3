# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_nums = sorted(nums)[::2]
        return sum(min_nums)
