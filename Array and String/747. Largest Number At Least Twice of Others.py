class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # find the max value and second maximum

        m1, m2, index = -1, -1, 0

        for i, num in enumerate(nums):
            if num > m1:
                m1, m2, index = num, m1, i
            elif num > m2:
                m2 = num
        return index if m1 >= m2 * 2 else -1