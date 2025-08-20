'''
The first version is to build a second loop.

'''
class Solution:
   def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if  nums[i] == nums[j]:
                        result += 1
        return result
'''
The Optimal solution is to use a dictionary to count the occurrences of each number.
HashMap Method
'''
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0 # num of Good Pairs
        num_count = {} # stores count of each number
        for num in nums:
            if  num in num_count: # number already seen before
                result += num_count[num] # form pairs with existing occurrences
                num_count[num] += 1 # increment count
            else:
                num_count[num] = 1 # first time seeing this number
        return result