
# the main point is to check the count that is add or even
class Solution(object):
    def canPermutePalindrome(self, s):
        hashset = set()
        
        for c in s:
            if c in hashset:
                hashset.remove(c)
            else:
                hashset.add(c)
        return len(hashset) <= 1
    


    # without use datastructure
    # from CTCL
    def is_palindrome_bit_vector(phrase):
        """checks if a string is a permutation of a palindrome"""
        #assume there is bit vector, each time we map the val into it.
        r = 0
        for c in phrase:
            val = ord(c)
            mask = 1 << val
            
            # there is repeated char
            if r & mask:
                r &= ~mask
            # no repeated number
            else:
                r |= mask
        # lastly check the bit vector has most one bit that set to 1.
        # If bit vector has more than one 1, it means there are two different val in phrase. Each bit means different char.
        return (r - 1) & r == 0
