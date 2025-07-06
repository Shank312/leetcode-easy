
class Solution:
    def isPalindrome(self, s):
        # step 1 : Filter only alphanumeric characters and convert to lowercase
        filtered = ''.join(c.lower() for c in s if c.isalnum())

        # step 2 : Compare the filtered string with its reverse
        return filtered == filtered[::-1]

sol = Solution()

print(sol.isPalindrome("A man, a plan, a canal : panama"))    # true
print(sol.isPalindrome("race a car"))                         # false
print(sol.isPalindrome(" "))                                  # true