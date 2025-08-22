'''
The first version:
'''class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                result.append(0)
            else:
                result.append(1)
        result.sort()
        return result
'''
The Second version:
'''
# class Solution:
#     def transformArray(self, nums: List[int]) -> List[int]:
#         count_even = 0
#         count_odd = 0
#         for i in range(len(nums)):
#             if nums[i] % 2 == 0:
#                 count_even += 1
#             else:
#                 count_odd += 1
#         result = [0] * count_even + [1] * count_odd
#         return result