class Solution:

    #imitating 
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

    #imitating 
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n-1, -1, -1):
            digits[i] = (digits[i] + 1) % 10
            if digits[i] != 0:
                return digits
        
        digits = [1] + digits
        return digits