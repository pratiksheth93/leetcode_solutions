# Time Complexity: O(N)
# Space Complexity: O(1)
"""
 We will start with one pointer pointing to the beginning of the array and another pointing at the end. At every step, we will see if the numbers pointed by the two pointers add up to the target sum. If they do, we have found our pair; otherwise, we will do one of two things:

    1) If the sum of the two numbers pointed by the two pointers is greater than the target sum, this means that we need a pair with a smaller sum. So, to try more pairs, we can decrement the end-pointer.

    2) If the sum of the two numbers pointed by the two pointers is smaller than the target sum, this means that we need a pair with a larger sum. So, to try more pairs, we can increment the start-pointer.
"""
class TwoPointerApproach:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        low, high = 0, len(arr) - 1
        i = 0
        while(i <= high):
            if arr[i] == 0:
                arr[i], arr[low] = arr[low], arr[i]
                # increment 'i' and 'low'
                i += 1
                low += 1
            elif arr[i] == 1:
                i += 1
            else:  # the case for arr[i] == 2
                arr[i], arr[high] = arr[high], arr[i]
                # decrement 'high' only, after the swap the number at index 'i' could be 0, 1 or 2
                high -= 1


# Time Complexity: O(N^2)
# Space Complexity: O(1)
"""
The brute force approach is simple. Loop through each element x and find if there is another value that equals to target − x
"""
class BruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
  

# Time Complexity: O(N)
# Space Complexity: O(1)
"""
While we are iterating and inserting elements into the hash table, we also look back to check if current element's complement already exists in the hash table. If it exists, we have found a solution and return the indices immediately.
"""
class HashTableApproach:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
 