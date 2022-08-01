# Time Complexity: O(N)
# Space Complexity: O(1)

class TwoPointer:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = min(height[left], height[right]) * (right - left)
        while right > left:
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

            max_area = max(min(height[left], height[right]) * (right - left), max_area)
        return max_area

# Time Complexity: O(N^2)
# Space Complexity: O(1)

class BruteForce:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                width = right - left
                maxarea = max(maxarea, min(height[left], height[right]) * width)

        return maxarea