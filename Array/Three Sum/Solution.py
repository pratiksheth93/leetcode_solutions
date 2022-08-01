# Time Complexity: O(N^2)
# Space Complexity: O(N)

class TwoPointers:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            if i == 0 or nums[i - 1] != nums[i]:
                while (lo < hi):
                    sum = nums[i] + nums[lo] + nums[hi]
                    if sum < 0:
                        lo += 1
                    elif sum > 0:
                        hi -= 1
                    else:
                        res.append([nums[i], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
        triplets = []
        for element in res:
            if element not in triplets:
                triplets.append(element)
        return triplets

 # Time Complexity: O(N^2)
# Space Complexity: O(N)
       
class HashSet:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1

 # Time Complexity: O(N^2)
# Space Complexity: O(N)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res
