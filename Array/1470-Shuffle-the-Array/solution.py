class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(len(nums)-n):
            j = i + n
            result.append(nums[i])
            result.append(nums[j])
        return result
# What I learned from this solution:
# The definition of shuffle is to rearrange the elements in a specific order.
# In this case, the optimal solution is:
#   for i in range(n):
#       result.append(nums[i])
#       result.append(nums[i+n])