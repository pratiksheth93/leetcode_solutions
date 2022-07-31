# Time Complexity: O(N)
# Space Complexity: O(N)

class DepthFirstSearch:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, [], 0, target, res)
        return res
    
    def dfs(self, nums, cur, start, remain, res):
        if remain == 0:
            res.append(cur[:])
            return
            
        for i in range(start, len(nums)):
            if nums[i] > remain:
                break
            cur.append(nums[i])
            self.dfs(nums, cur, i, remain - nums[i], res)
            cur.pop()

# Time Complexity: O(N^ (T/M+1))
# Space Complexity: O(T/M)
# N: Number of candidates, T: Target Value, M: Minimal Value among candidates
class Backtrack:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results
