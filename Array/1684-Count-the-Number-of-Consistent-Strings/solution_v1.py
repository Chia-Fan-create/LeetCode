class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        HashMap_a ={}
        count = 0
        for char in allowed:
            if char in HashMap_a:
                HashMap_a[char] += 1
            else:
                HashMap_a[char] = 1
        allowed_keys = list(HashMap_a.keys())
        for i in range(len(words)):
            HashMap_w = {}
            for char in words[i]:
                if char in HashMap_w:
                    HashMap_w[char] += 1
                else:
                    HashMap_w[char] = 1
                words_keys = list(HashMap_w.keys())
            if set(words_keys) <= set(allowed_keys):
                count += 1
        return count
