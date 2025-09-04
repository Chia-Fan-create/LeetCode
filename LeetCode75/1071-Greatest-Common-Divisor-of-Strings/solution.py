# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         if str1 in str2: # problem 
#             for i in range(1,len(str2)):
#                 if str2[i] == str2[0]:
#                     return str2[0:i]
#                 elif # How to write if there's no GCD
#         elif str2 in str1: # problem
#             for j in range(1,len(str1)):
#                 if str1[j] == str1[0]:
#                     return str1[0:j]
#                 elif # How to write if there's no GCD
#         else:
#             return ""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they have a common divisor
        if str1 + str2 != str2 +str1: 
            return ""
        # Euclidean algorithm
        if len(str1) == len(str2):
            return str1
        # Reduce the longer string
        if len(str1) > len(str2):
            # Cut str1 by the length of str2
            return self.gcdOfStrings(str1[len(str2):], str2)
        else:
            # Cut str2 by the length of str1
            return self.gcdOfStrings(str1, str2[len(str1):])
# Time complexity: O(n + m) where n and m are the lengths of str1 and str2 respectively.
# Space complexity: O(n + m) in the worst case due to the recursion stack.

# Alternative solution
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        # Check if they have a common divisor
        def valid(k):
            if len1 % k or len2 % k: # k must divide both lengths
                return False
            n1, n2 = len1 // k, len2 // k # How many times the base string should repeat
            base = str1[:k] # Candidate base string
            return str1 == n1 * base and str2 == n2 * base # Check if both strings can be formed by repeating the base string
        # Iterate from the minimum length down to 1
        for i in range(min(len1, len2), 0, -1): # Start from the largest possible divisor
            if valid(i): # If valid, return the base string
                return str1[:i] # Return the base string
        return "" # If no common divisor found, return empty string
# Time complexity: O(n * sqrt(min(n, m)))) where n and m are the lengths of str1 and str2 respectively.
# Space complexity: O(1) as we are using a constant amount of extra space.