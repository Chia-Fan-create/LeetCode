from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rMap = collections.Counter(ransomNote)
        mMap = collections.Counter(magazine)
        for key in rMap:
            if key not in mMap:
                return False
            if mMap[key] < rMap[key]:
                return False
        return True
    
# What I learned from this implementation
# 1. Using Counter from collections is a concise way to count character frequencies.
# 2. The position of if and return statements can affect the flow of logic and performance.