# Time Complexity: O(N^(K-1))
# Space Complexity: O(N)

"""
We can implement k - 2 loops using a recursion. We will pass the starting point and k as the parameters. When k == 2, we will call twoSum, terminating the recursion.

1. For the main function:

    - Sort the input array nums.
    -   Call kSum with start = 0, k = 4, and target, and return the result.

2. For kSum function:

    - At the start of the kSum function, we will check three conditions:
        a. Have we run out of numbers to choose from?
        b. Is the smallest number remaining greater than target / k? 
            If so, then any k numbers we choose will be too large.
        c. Is the largest number remaining smaller than target / k? 
            If so, then any k numbers we choose will be too small.
        If any of these conditions is true, there is no need to continue as no combination of the remaining elements can sum to target.
    
    - If k equals 2, call twoSum and return the result.
    - Iterate i through the array from start:
        a. If the current value is the same as the one before, skip it.
        b. Recursively call kSum with start = i + 1, k = k - 1, and target - nums[i].
        c. For each returned subset of values:
            Include the current value nums[i] into subset.
            Add subset to the result res.

    - Return the result res.

3. For twoSum function:

    - Set the low pointer lo to start, and high pointer hi to the last index.
    - While low pointer is smaller than high:
        a. If the sum of nums[lo] and nums[hi] is less than target, increment lo.
            Also increment lo if the value is the same as for lo - 1.
        b. If the sum is greater than target, decrement hi.
            Also decrement hi if the value is the same as for hi + 1.
        c. Otherwise, we found a pair:
            Add it to the result res.
            Decrement hi and increment lo.
    - Return the result res.

"""


class HashSet:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            result = []
            s = set()
            for i in range(len(nums)):
                if len(result) == 0 or result[-1][1]!= nums[i]:
                    if target - nums[i] in s:
                        result.append([target - nums[i], nums[i]])
                s.add(nums[i])
            return result
        
        def kSum(nums: List[int], target: int, k:int) -> List[List[int]]:
            result = []
            if not nums:
                return result
            average = target //k
            if average < nums[0] or nums[-1] < average:
                return result
            
            if k == 2:
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i-1]!= nums[i]:
                    for subset in kSum(nums[i+1:], target - nums[i], k-1):
                        result.append([nums[i]] + subset)
            return result
        
        nums.sort()
        return kSum(nums, target, 4) 