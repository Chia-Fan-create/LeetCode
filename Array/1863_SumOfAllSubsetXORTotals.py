'''
Hard!!!
Use Bit manipulation

'''class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result |= num # take the running OR of result and num
        return result << (len(nums)-1) # Append (N-1) zeros to the right of the binary representation of result by shifting result by (N-1) places


