class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def check(word): # check if the word is consistent
            for char in word:
                if char not in allowed:
                    return False
            return True

        count = 0
        for word in words:
            if check(word):
                count += 1
        return count
