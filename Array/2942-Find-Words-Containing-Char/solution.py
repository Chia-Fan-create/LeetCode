'''
This is version 1 of the function.

'''

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        count = []
        for i in range(len(words)):
            if x in words[i]:
                count.append(i)
        return count
    
'''
This is version 2 of the function.
Learn enumerate function
'''
# class Solution:
#     def findWordsContaining(self, words: List[str], x: str) -> List[int]:
#         output = []
#         for i, word in enumerate(words):
#             if x in word:
#                 output.append(i)
#         return output
'''
This is version 3 of the function.
Learn how to write one line programming
'''
# class Solution:
#     def findWordsContaining(self, words: List[str], x: str) -> List[int]:
#         return [i for i, word in enumerate(words)if x in word]
    