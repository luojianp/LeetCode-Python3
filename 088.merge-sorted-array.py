# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m+n):
            nums1[i] = nums2[i-m]

        nums1.sort()


nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
Solution().merge(nums1, 6, [1, 2, 2], 3)
print(nums1)
