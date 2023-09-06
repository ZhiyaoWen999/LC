class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1

        while index >= 0 and digits == 9:
            digits[index] = 0
            index -= 1
        if index >= 0:
            digits[index] += 1
        else:
            digits = [1] + digits
        return digits