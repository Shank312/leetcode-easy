
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j]!=nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
    
   # Test input
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  

   # Create object and call method
sol =  Solution()
k = sol.removeDuplicates(nums)

   # Print output in Leetcode-style format
print("k =", k)
print("Modified nums (first k elements):", nums[:k])


        