## Author: ZhiyaoWen

## Find the target in a matrix, it is different with 378, which to find the Kth number.

from typing import List

class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = left +(right - left) // 2
            cur = matrix[mid // n][mid % n]

            if cur == target:
                return True
            elif cur < target:
                left = mid + 1
            else:
                right = mid - 1
        return False