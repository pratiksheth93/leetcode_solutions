# Time Complexity: O(N)
# Space Complexity: O(1)
"""
Kadane Algorithm

    1. Initialize 2 integer variables. Set both of them equal to the first value in the array.
            - currentSubarray will keep the running count of the current subarray we are focusing on.
            - maxSubarray will be our final return value. Continuously update it whenever we find a bigger subarray.
    2. Iterate through the array, starting with the 2nd element (as we used the first element to initialize our variables). For each number, add it to the currentSubarray we are building. If currentSubarray becomes negative, we know it isn't worth keeping, so throw it away. Remember to update maxSubarray every time we find a new maximum.

    3. Return maxSubarray.
"""
class Dynamic Programming:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]
        
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray

# Time Complexity: O(N*Log N)
# Space Complexity: O(Log N)

"""
    1. Define a helper function that we will use for recursion.

        - This function will take an input left and right, which defines the bounds of the array. The return value of this function will be the best possible subarray for the array that fits between left and right.
        - If left > right, we have an empty array. Return negative infinity.
        - Find the midpoint of our array. This is (left + right) / 2, rounded down. Using this midpoint, find the best possible subarray that uses elements from both sides of the array with the algorithm detailed in the animation above.
        - The best subarray using elements from both sides is only 1 of 3 possibilities. We still need to find the best subarray using only the left or right halves. So, call this function again, once with the left half, and once with the right half.
        - Return the largest of the 3 values - the best left half sum, the best right half sum, and the best combined sum.

    2. Call our helper function with the entire input array (left = 0, right = length - 1). This is our final answer, so return it.
"""
class DivideAndConquer:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)
        
        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)


# Time Complexity: O(N^2)
# Space Complexity: O(1)

"""
    1. Initialize a variable maxSubarray = -infinity to keep track of the best subarray. We need to use negative infinity, not 0, because it is possible that there are only negative numbers in the array.

    2. Use a for loop that considers each index of the array as a starting point.

    3. For each starting point, create a variable currentSubarray = 0. Then, loop through the array from the starting index, adding each element to currentSubarray. Every time we add an element it represents a possible subarray - so continuously update maxSubarray to contain the maximum out of the currentSubarray and itself.

    4. Return maxSubarray.
"""
class BruteForce:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray
