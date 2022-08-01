# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def isValidSubsequence(self, array:List[int], sequence:List[int]) -> bool:
        index = 0
	    for value in array:
		    if index == len(sequence):
			    break
		    if sequence[index] == value:
			    index+=1
	    return index == len(sequence)
