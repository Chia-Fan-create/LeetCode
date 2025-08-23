class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] % 3 != 0:
                count += 1
        return count
# What I learned from this solution:
# The different between:
#    for i in nums:
#       if i % 3 != 0:
#           count += 1
#-----
#    for i in range(len(nums)):
#       if nums[i] % 3 != 0:
#           count += 1
#