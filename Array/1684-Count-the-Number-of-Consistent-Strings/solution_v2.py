class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        Char_a = []
        count = 0
        for char in allowed:
            if char in Char_a:
                pass
            else:
                Char_a.append(char)
        for i in range(len(words)):
            Char_w =[]
            for char in words[i]:
                if char in Char_w:
                    pass
                else:
                    Char_w.append(char)
            if set(Char_w) <= set(Char_a):
                count += 1
        return count
