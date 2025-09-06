class Solution:
    def reverseVowels(self, s: str) -> str:
        # Use two pointers to reverse the vowels in the string
        vowels = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left] # Swap the vowels
                left += 1
                right -= 1
        return ''.join(s) # Convert list back to string and return

# complexity analysis
# Time complexity: O(n) - We traverse the string at most once with two pointers.
# Space complexity: O(n) - We convert the string to a list to allow in-place modifications.