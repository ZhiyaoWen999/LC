class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        n = len(nums)
        
        sumleft = 0

        for i in range(n):
            if 2 * subleft + nums[i] == total:
                return i
            subleft += nums[i]
        return -1