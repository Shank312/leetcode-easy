
from typing import List

class Solution:
    def maxSubArray(self, nums):
     max_sum = current_sum = nums[0]
     for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
     return max_sum


# Simple test input
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Create instance and class method
sol = Solution()
result = sol.maxSubArray(nums)

# print output
print("Maximum subarray sum:", result)
