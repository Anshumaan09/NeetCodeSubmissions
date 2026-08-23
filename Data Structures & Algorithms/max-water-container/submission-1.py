class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # assign pointers
        left = 0
        right = len(heights) - 1
        max_storage = 0

        # Core logic
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            curr_storage = height * width
            max_storage = max(curr_storage, max_storage)

            # Move the pointers
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_storage