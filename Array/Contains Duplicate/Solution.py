# Time Complexity: O(N)
# Space Complexity: O(N)

class HashMap:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for num in nums:
            if num in seen:
                return True
            seen[num]=1
        return False
