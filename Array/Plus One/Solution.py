# Time Complexity: O(N)
# Space Complexity: O(N)

"""
1. Move along the input array starting from the end of array.
2. Set all the nines at the end of array to zero.
3. If we meet a not-nine digit, we would increase it by one. The job is done - return digits.
4. We're here because all the digits were equal to nine. Now they have all been set to zero. We then append the digit 1 in front of the other digits and return the result.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n):
            idx = n - 1 - i
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits

        return [1] + digits
