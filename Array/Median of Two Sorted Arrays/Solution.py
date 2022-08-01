# Time Complexity: O(log (n+m))
# Space Complexity: O(n+m)
# n: len(num1), m: len(num2)


class TwoPointer:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        idx_1 = 0
        idx_2 = 0
        result=[]

        while (idx_1 < len(num1)) and (idx_2 < len(num2)):
            if num1[idx_1] <= num2[idx_2]:
                result.append(num1[idx_1])
                idx_1 +=1
            else:
                result.append(num2[idx_2])
                idx_2 +=1

        while idx_2 < len(num2):
            result.append(num2[idx_2])
            idx_2+=1

        while idx_1 < len(num1):
            result.append(num1[idx_1])
            idx_1+=1

        mid_point = len(result) // 2
        return (result[mid_point]+result[~mid_point]) / 2
        
# Time Complexity: O(n+m)
# Space Complexity: O(n+m)
# n: len(num1), m: len(num2)

class Sorting:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = sorted(nums1+nums2)
        mid = int(len(l)/2)
        if len(l)%2 == 1:
            return l[mid]
        return sum(l[mid-1:mid+1])/2