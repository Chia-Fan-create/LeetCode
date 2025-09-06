class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a','e','i','o','u','A','E','I','O','U']
        vowels = {}
        # store the index and value of vowels in the string
        for i in range(len(s)):
            if s[i] in v:
                vowels[i] = s[i]
        get_vowels_value = list(vowels.values()) # get the values of the vowels
        re_vowels = get_vowels_value[::-1] # reverse the values of the vowels
        # change the value of the vowels in the original string
        def change_char_at_index(origin, char, index):
            new = origin[:index]+ char + origin[index+1:] # slice the string and replace the char at index
            return new
        j = 0
        # replace the vowels in the original string with the reversed vowels
        for i in vowels.keys():
            s = change_char_at_index(s,re_vowels[j],i)
            j += 1
        return s
# complexity analysis
# Time complexity: O(n) - We traverse the string multiple times but each traversal is O(n).
# Space complexity: O(n) - We use extra space to store the vowels and their indices.
