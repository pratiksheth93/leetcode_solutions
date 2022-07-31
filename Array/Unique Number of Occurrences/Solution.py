# Time Complexity: O(N Log N)
# Space Complexity: O(N)

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen={}
        for i in range(len(arr)):
            if arr[i] not in seen:
                seen[arr[i]]=1
            else:
                seen[arr[i]]+=1
                
        value_set=[]
        for element in seen.values():
            if element in value_set:
                return False
            else:
                value_set.append(element)
        
        return True

